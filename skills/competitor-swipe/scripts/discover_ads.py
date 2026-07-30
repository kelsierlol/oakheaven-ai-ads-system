#!/usr/bin/env python3
"""
Turns a Facebook Ads Library "view all" / search listing URL (or a bare page ID)
into a list of individual ad links, by loading the page in a real headless
browser, scrolling until no new ads load, and extracting ad IDs from the
rendered page's own state (same technique as the browser-console bookmarklet
approach: read `ad_library_id` out of the page, don't hit any private API
directly).

Usage:
    python3 discover_ads.py "<listing_url_or_page_id>" [--limit N] [--out links.txt]

If given a bare numeric page ID, builds the standard "view all ads for this
page" listing URL automatically.
"""
import argparse
import re
import sys
import time

from playwright.sync_api import sync_playwright

AD_ID_RE = re.compile(r'"ad_archive_id"\s*:\s*"?(\d+)"?')


def build_listing_url(page_id_or_url):
    if page_id_or_url.isdigit():
        return (
            "https://www.facebook.com/ads/library/"
            "?active_status=all&ad_type=all&country=ALL"
            "&is_targeted_country=false&media_type=all&search_type=page"
            "&sort_data[direction]=desc&sort_data[mode]=total_impressions"
            f"&view_all_page_id={page_id_or_url}"
        )
    return page_id_or_url


def discover(listing_url, limit=None, max_idle_scrolls=4, max_scrolls=200):
    ids_seen = []
    ids_set = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
            )
        )
        page.goto(listing_url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)

        idle_rounds = 0
        for scroll_i in range(max_scrolls):
            html = page.content()
            found = AD_ID_RE.findall(html)
            new_count = 0
            for ad_id in found:
                if ad_id not in ids_set:
                    ids_set.add(ad_id)
                    ids_seen.append(ad_id)
                    new_count += 1

            if limit and len(ids_seen) >= limit:
                break

            if new_count == 0:
                idle_rounds += 1
                if idle_rounds >= max_idle_scrolls:
                    break
            else:
                idle_rounds = 0

            page.mouse.wheel(0, 4000)
            page.wait_for_timeout(1500)

        browser.close()

    if limit:
        ids_seen = ids_seen[:limit]
    return ids_seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("listing_url_or_page_id")
    ap.add_argument("--limit", type=int, default=None, help="max ads to return")
    ap.add_argument("--out", default=None, help="write links to this file, one per line")
    args = ap.parse_args()

    url = build_listing_url(args.listing_url_or_page_id)
    print(f"Loading listing: {url}", file=sys.stderr)

    ids = discover(url, limit=args.limit)

    if not ids:
        print(
            "No ad IDs found. The page may require a real logged-in session, "
            "may have zero active ads, or Facebook may be serving a challenge "
            "page. Try opening the link in a real browser to confirm ads exist.",
            file=sys.stderr,
        )
        sys.exit(1)

    links = [f"https://www.facebook.com/ads/library/?id={i}" for i in ids]

    if args.out:
        with open(args.out, "w") as f:
            f.write("\n".join(links) + "\n")
        print(f"Wrote {len(links)} links to {args.out}", file=sys.stderr)
    else:
        print("\n".join(links))

    print(f"Found {len(links)} ads.", file=sys.stderr)


if __name__ == "__main__":
    main()
