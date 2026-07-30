---
name: competitor-swipe
description: Use this skill whenever the user pastes a Facebook Ads Library link — either a single ad link (contains "?id=") or a page/search listing link (contains "view_all_page_id=" or a bare Facebook page ID) — and wants ads downloaded and analyzed, or asks to "rip this ad", "swipe this ad", "pull this competitor's ad library", "rip this page's ads", "add this to the swipe file", or "analyze this competitor's copy". Discovers individual ad links from a listing page if needed, downloads each ad video, extracts the caption, transcribes the video with mandatory timestamps, saves everything into an organized swipe folder, and (on request) breaks down the hook/copy structure. Do NOT use this for writing new ad scripts — that's script-generator. This only rips and analyzes what already exists.
---

# Competitor Swipe Ripper

Turns a Facebook Ads Library link — single ad OR a whole page's ad listing — into fully organized, analyzable swipe files: video + caption + timestamped transcript per ad.

## Two entry points

1. **Single ad link** (`.../ads/library/?id=123...`) → skip straight to Step 1 (Rip).
2. **Page/listing link** (`.../ads/library/?...view_all_page_id=123...`) or a bare Facebook page ID → run Step 0 (Discover) first to turn it into a list of individual ad links, then feed all of them through Step 1.

## Non-negotiable rule: timestamps

Every transcript this skill produces MUST have per-segment start/end timestamps. Never output a transcript as a single wall of text and never strip timestamps to "clean it up." Timestamps are the only way to measure:

- **Hook length** — how many seconds before the first pattern interrupt / claim
- **Time-to-offer** — when the actual offer/mechanism gets introduced
- **Time-to-CTA** — when they ask for the click/call
- **Pacing** — words per second, cut frequency implied by topic shifts

Without timestamps this whole exercise is just "reading an ad," not building a swipe file you can benchmark against your own client's account metrics. If a transcription step ever returns text with no timestamps, treat that as a failed run — do not save it, re-run it.

## Step 0 — Discover ad links from a page/listing (only when given a listing link or page ID)

A listing URL (e.g. `.../ads/library/?...&view_all_page_id=126546490551375`) contains no ad data itself — Facebook injects it client-side via JS after load. A plain fetch/curl/yt-dlp will get a 403 or empty page. This step uses a real headless browser to load and scroll the page, then reads the ad IDs out of the rendered page (`ad_archive_id` fields), the same way a browser console script would — it does not call any private/authenticated API directly.

```bash
python3 scripts/discover_ads.py "<listing_url_or_bare_page_id>" --out links.txt
```

Requires `playwright` in the venv (`pip install playwright && python3 -m playwright install chromium` — one-time setup; skip the install step if Chromium is already cached under `~/Library/Caches/ms-playwright`).

Notes:
- Pass just the numeric page ID if that's all the user gives you — the script builds the full listing URL itself.
- Add `--limit N` to cap discovery (e.g. top 10 by impressions, since the default listing URL sorts by `total_impressions` desc).
- If it returns zero ads, don't assume the script is broken — check whether the page genuinely has no active ads, or whether Facebook served a challenge/consent page (rare but possible; report this to the user rather than retrying silently).
- Feed every link in `links.txt` into Step 1, one rip_ad.py call per link. Don't stop the batch if one fails — same rule as multi-link batches below.

## Step 1 — Rip the ad

Ask the user (if not already given) for:
1. The Facebook Ads Library URL(s)
2. Which **client** this competitor research is for
3. The competitor **business name**
4. Owner/founder name and website, if known (optional but include when given)

Run, per link:

```bash
python3 scripts/rip_ad.py "<fb_ads_library_url>" \
  --client "<client name>" \
  --business "<competitor business>" \
  --owner "<owner name>" \
  --website "<website>" \
  --swipes-root "swipes"
```

This requires `yt-dlp`, `ffmpeg`, and a Python venv with `faster-whisper` installed. If the venv doesn't exist yet, set it up once:

```bash
python3 -m venv venv && source venv/bin/activate && pip install faster-whisper
```

then run the script with that venv's `python3`.

Handle failures explicitly, don't paper over them:
- **Image-only / carousel ad, no video** — yt-dlp will fail to find a video stream. Still capture the caption + image, note in `ad.md` that this is a static ad with no transcript (timestamps don't apply here — that's fine, it's a different ad type, not a skipped step).
- **Ad removed / region-locked** — report to the user which ad_id failed and move on to the next link.
- **Multiple links pasted at once** — process each one, don't stop the batch on a single failure.

## Step 2 — Output structure

```
swipes/
  <client>/
    index.md                          ← running table of every ad ripped for this client
    <competitor-business>/
      <hook-slug>_<ad_id>/
        video.mp4
        ad.json
        ad.md                         ← includes the timestamped transcript
```

`ad.json` is the source of truth (structured, timestamps included). `ad.md` is the human-skimmable version for quickly reading copy. `index.md` lets you scan a client's whole competitor library without opening folders.

## Step 3 — Copy analysis (on request)

If the user asks to analyze/break down the copy (not just rip it), read the `ad.json` transcript and produce, using the timestamps directly:

- **Hook (0s → first interrupt):** what it is, why it stops the scroll
- **Structure:** problem → agitation → mechanism → proof → offer → CTA, with the timestamp where each beat starts
- **Angle:** the core belief/fear/desire being sold to
- **Proof stack used:** stats, testimonials, credentials — quote them with timestamp
- **CTA:** exact wording and when it lands

Ground every claim in a timestamp — "hook runs 0:00–0:07" not "the hook is short." That's the entire reason timestamps are mandatory in step 1.
