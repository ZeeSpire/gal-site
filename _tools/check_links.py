#!/usr/bin/env python3
"""Parse every committed HTML file and verify every internal href/src resolves
to an existing file on disk. External (http(s):, mailto:, javascript:) and
in-page anchor links are reported but not validated against the filesystem.

Usage:
    python3 _tools/check_links.py
Exit code 0 if no broken internal references, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HREF_RE = re.compile(r'(?:href|src)="([^"#][^"]*)"', re.IGNORECASE)
STYLE_URL_RE = re.compile(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)""", re.IGNORECASE)

# Links that are intentionally broken in the source and stay broken in the static
# rebuild until the missing upstream file is restored.
EXPECTED_BROKEN: set[str] = set()


def is_external(url: str) -> bool:
    return bool(re.match(r"^(https?:|mailto:|tel:|javascript:|data:)", url, re.I))


def normalise(url: str) -> str:
    url = url.split("#", 1)[0].split("?", 1)[0]
    return urllib.parse.unquote(url)


def main() -> int:
    htmls = sorted(ROOT.rglob("*.html"))
    htmls = [h for h in htmls if "_tools" not in h.parts]
    broken: list[tuple[Path, str, Path]] = []
    expected_skipped: list[tuple[Path, str]] = []
    checked_internal = 0
    external_count = 0

    for html in htmls:
        text = html.read_text(encoding="utf-8")
        refs = [m.group(1) for m in HREF_RE.finditer(text)]
        refs += [m.group(1) for m in STYLE_URL_RE.finditer(text)]
        for url in refs:
            url = url.strip()
            if not url:
                continue
            if is_external(url):
                external_count += 1
                continue
            target = (html.parent / normalise(url)).resolve()
            if target.is_dir():
                target = target / "index.html"
            try:
                rel_from_root = target.relative_to(ROOT).as_posix()
            except ValueError:
                rel_from_root = str(target)
            if not target.exists():
                if rel_from_root in EXPECTED_BROKEN:
                    expected_skipped.append((html.relative_to(ROOT), url))
                else:
                    broken.append((html.relative_to(ROOT), url, target))
            checked_internal += 1

    print(f"HTML files scanned: {len(htmls)}")
    print(f"Internal refs verified: {checked_internal}")
    print(f"External refs skipped: {external_count}")
    if expected_skipped:
        print(f"Expected-broken (logged in SPEC Deviations): {len(expected_skipped)}")
        for src, url in expected_skipped:
            print(f"  {src}: {url!r}  (expected)")

    if broken:
        print(f"\nBROKEN internal references: {len(broken)}")
        for src, url, resolved in broken:
            print(f"  {src}: {url!r}  ->  {resolved}")
        return 1

    print("\nAll internal references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
