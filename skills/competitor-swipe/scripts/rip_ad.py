#!/usr/bin/env python3
"""
Rips a Facebook Ads Library ad: downloads video + caption, transcribes with
timestamps, and writes ad.json + ad.md into a swipe folder.

Usage:
    python3 rip_ad.py <fb_ads_library_url> \
        --client "<sophron client name>" \
        --business "<competitor business name>" \
        --owner "<optional owner/founder name>" \
        --website "<optional website>" \
        --swipes-root "<path to swipes/ folder>"

Timestamps on the transcript are NOT optional. They are the whole point:
without them you cannot measure hook length, time-to-offer, time-to-CTA,
or pacing against your own account's metrics. Never strip them, never
collapse segments into a single blob of text.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def slugify(text, max_words=6):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    words = text.split()[:max_words]
    return "-".join(words) if words else "untitled"


def fmt_ts(seconds):
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m}:{s:02d}"


class NoVideoAd(Exception):
    def __init__(self, info):
        self.info = info
        super().__init__("Ad has no video (image-only or carousel ad).")


def scrape_image_ad_via_browser(url):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
            )
        )
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(2000)
        html = page.content()
        browser.close()

    page_names = re.findall(r'"page_name"\s*:\s*"([^"]+)"', html)
    bodies = re.findall(r'"body"\s*:\s*\{\s*"text"\s*:\s*"((?:[^"\\]|\\.)*)"', html)

    def unescape(s):
        try:
            return json.loads(f'"{s}"')
        except json.JSONDecodeError:
            return s

    page_name = unescape(page_names[0]) if page_names else ""
    caption = unescape(bodies[0]) if bodies else ""
    return page_name, caption


def run_ytdlp(url, workdir):
    result = subprocess.run(
        [
            "yt-dlp", url,
            "-o", "video.%(ext)s",
            "--write-description",
            "--write-info-json",
        ],
        cwd=workdir,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        if "No video formats found" in result.stderr:
            meta_result = subprocess.run(
                ["yt-dlp", url, "--skip-download", "--write-info-json",
                 "-o", "video.%(ext)s"],
                cwd=workdir,
                capture_output=True,
                text=True,
            )
            info_path = workdir / "video.info.json"
            if meta_result.returncode == 0 and info_path.exists():
                raise NoVideoAd(json.loads(info_path.read_text()))
            raise NoVideoAd({})
        raise subprocess.CalledProcessError(
            result.returncode, result.args, output=result.stdout, stderr=result.stderr
        )

    info = json.loads((workdir / "video.info.json").read_text())
    video_file = [f for f in workdir.glob("video.*") if f.suffix != ".json" and f.suffix != ".description"][0]
    return info, video_file.name


class NoAudioTrack(Exception):
    pass


def transcribe(video_path):
    from faster_whisper import WhisperModel

    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a",
         "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(video_path)],
        capture_output=True, text=True,
    )
    if not probe.stdout.strip():
        raise NoAudioTrack("Video has no audio stream — silent motion graphic, not a speech ad.")

    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(video_path), word_timestamps=False)
    out = []
    for seg in segments:
        out.append({
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "text": seg.text.strip(),
        })
    if not out:
        raise RuntimeError(
            "Transcription produced zero segments. Ad may be silent/image-only. "
            "Do not fabricate a transcript — mark this ad as image/no-speech instead."
        )
    return out


def build_md(meta, caption, transcript, silent=False, is_image_ad=False):
    lines = [
        f"# {meta['business']} — {meta['title']}",
        "",
        f"- **Owner:** {meta.get('owner') or 'unknown'}",
        f"- **Website:** {meta.get('website') or 'unknown'}",
        f"- **Ad ID:** {meta['ad_id']}",
        f"- **Source:** {meta['source_url']}",
        f"- **Video:** {'(image ad, no video)' if is_image_ad else '`video.mp4`'}",
        "",
        "## Caption",
        "",
        caption or "(no caption captured)",
        "",
    ]
    if is_image_ad:
        lines += [
            "## Transcript",
            "",
            "(Image-only ad — no video to transcribe. Analyze on caption + creative image only.)",
        ]
        return "\n".join(lines) + "\n"
    if silent:
        lines += [
            "## Transcript",
            "",
            "(No audio track — silent motion graphic / text-only ad. No transcript to fabricate; "
            "analyze this one on caption + visual copy only.)",
        ]
    else:
        lines += ["## Transcript (timestamped — required for hook/pacing metrics)", ""]
        for seg in transcript:
            lines.append(f"- **[{fmt_ts(seg['start'])} - {fmt_ts(seg['end'])}]** {seg['text']}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--client", required=True)
    ap.add_argument("--business", required=True)
    ap.add_argument("--owner", default="")
    ap.add_argument("--website", default="")
    ap.add_argument("--swipes-root", required=True)
    args = ap.parse_args()

    ad_id_match = re.search(r"id=(\d+)", args.url)
    ad_id = ad_id_match.group(1) if ad_id_match else "unknown"

    tmp_dir = Path(args.swipes_root) / "_tmp" / ad_id
    tmp_dir.mkdir(parents=True, exist_ok=True)

    print(f"[1/3] Downloading video + caption for ad {ad_id}...")
    is_image_ad = False
    video_filename = None
    try:
        info, video_filename = run_ytdlp(args.url, tmp_dir)
        caption = info.get("description", "")
        title = info.get("title") or slugify(caption[:60]).replace("-", " ").title() or "Untitled Ad"
    except NoVideoAd:
        print("    -> No video formats — image-only ad. Scraping caption via browser instead.")
        is_image_ad = True
        page_name, caption = scrape_image_ad_via_browser(args.url)
        title = slugify(caption[:60]).replace("-", " ").title() or "Untitled Ad"
        if page_name and not args.owner:
            args.owner = page_name

    silent = is_image_ad
    if is_image_ad:
        transcript = []
    else:
        print("[2/3] Transcribing with timestamps (required, not skippable)...")
        try:
            transcript = transcribe(tmp_dir / video_filename)
        except NoAudioTrack as e:
            print(f"    -> {e} Saving as silent/no-speech ad, no fabricated transcript.")
            transcript = []
            silent = True

    hook_slug = slugify(title)
    final_dir = Path(args.swipes_root) / args.client / args.business / f"{hook_slug}_{ad_id}"
    final_dir.mkdir(parents=True, exist_ok=True)

    if not is_image_ad:
        (tmp_dir / video_filename).rename(final_dir / "video.mp4")

    meta = {
        "ad_id": ad_id,
        "client": args.client,
        "business": args.business,
        "owner": args.owner,
        "website": args.website,
        "source_url": args.url,
        "title": title,
    }

    ad_json = {
        **meta,
        "caption": caption,
        "video_file": None if is_image_ad else "video.mp4",
        "is_image_ad": is_image_ad,
        "silent": silent,
        "transcript": transcript,
    }
    (final_dir / "ad.json").write_text(json.dumps(ad_json, indent=2))
    (final_dir / "ad.md").write_text(build_md(meta, caption, transcript, silent=silent, is_image_ad=is_image_ad))

    for leftover in tmp_dir.glob("*"):
        leftover.unlink()
    tmp_dir.rmdir()

    print(f"[3/3] Saved to {final_dir}")

    index_path = Path(args.swipes_root) / args.client / "index.md"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    if not index_path.exists():
        index_path.write_text("| Date Ripped | Business | Hook / Title | Ad ID | Folder |\n|---|---|---|---|---|\n")
    with index_path.open("a") as f:
        rel = final_dir.relative_to(index_path.parent)
        f.write(f"| | {args.business} | {title} | {ad_id} | `{rel}` |\n")


if __name__ == "__main__":
    main()
