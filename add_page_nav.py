#!/usr/bin/env python3
"""
add_page_nav.py — inject a "← Previous / Contents / Next →" bar into each built
lesson page in docs/sessions/.

The lesson ORDER is read directly from docs/index.html (the contents page is the
single source of truth), so reordering or adding sessions there and re-running
keeps the nav correct. Only sessions that are actually linked (built) in
index.html are chained — "coming soon" entries are <span>, not <a>, so they are
skipped automatically. As you build more pages and turn their index entries into
links, re-run this to rewire the chain.

Idempotent: the block is wrapped in <!-- PAGE-NAV-START/END --> markers and
replaced (not duplicated) on re-run.

Usage:
    python3 add_page_nav.py          # write nav into all built lesson pages
    python3 add_page_nav.py --check  # dry run: print the detected order, write nothing
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "docs" / "index.html"
SESSIONS_DIR = ROOT / "docs" / "sessions"

NAV_START = "<!-- PAGE-NAV-START -->"
NAV_END = "<!-- PAGE-NAV-END -->"


def strip_tags(s: str) -> str:
    """Remove any HTML tags (e.g. the 'built' badge span) and collapse whitespace."""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def detected_order():
    """Return [(filename, title), ...] for built session links, in document order."""
    html = INDEX.read_text(encoding="utf-8")
    pairs = []
    for m in re.finditer(r'<a[^>]*href="sessions/([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL):
        filename, inner = m.group(1), m.group(2)
        # drop the "built" badge (tag + its text) before extracting the title
        inner = re.sub(r'<span class="badge-built">.*?</span>', "", inner, flags=re.DOTALL)
        if (SESSIONS_DIR / filename).exists():
            pairs.append((filename, strip_tags(inner)))
    return pairs


def nav_cell(kind, href, label, title):
    return (
        f'  <a class="{kind}" href="{href}">'
        f'<span class="nav-label">{label}</span>'
        f'<span class="nav-title">{title}</span></a>'
    )


def build_nav(prev, nxt):
    left = (
        nav_cell("prev", prev[0], "← Previous", prev[1])
        if prev
        else '  <span class="nav-empty"></span>'
    )
    home = '  <a class="home" href="../index.html"><span class="nav-title">⌂</span></a>'
    right = (
        nav_cell("next", nxt[0], "Next →", nxt[1])
        if nxt
        else '  <span class="nav-empty"></span>'
    )
    return f"{NAV_START}\n<nav class=\"page-nav\">\n{left}\n{home}\n{right}\n</nav>\n{NAV_END}"


def inject(html: str, nav: str) -> str:
    # remove any existing nav block (idempotent)
    html = re.sub(
        re.escape(NAV_START) + r".*?" + re.escape(NAV_END) + r"\n?",
        "",
        html,
        flags=re.DOTALL,
    )
    # insert before the container's closing </div> that precedes </body>
    body_idx = html.find("</body>")
    if body_idx == -1:
        raise ValueError("no </body> found")
    div_idx = html.rfind("</div>", 0, body_idx)
    if div_idx == -1:
        raise ValueError("no closing </div> before </body>")
    return html[:div_idx] + nav + "\n" + html[div_idx:]


def main():
    check = "--check" in sys.argv
    order = detected_order()

    print(f"Detected {len(order)} built session(s) in index.html order:")
    for i, (fn, title) in enumerate(order):
        print(f"  {i + 1}. {title}  [{fn}]")
    if not order:
        print("Nothing to do.")
        return

    if check:
        print("\n--check: no files written.")
        return

    for i, (fn, _) in enumerate(order):
        prev = order[i - 1] if i > 0 else None
        nxt = order[i + 1] if i < len(order) - 1 else None
        path = SESSIONS_DIR / fn
        html = path.read_text(encoding="utf-8")
        path.write_text(inject(html, build_nav(prev, nxt)), encoding="utf-8")
        print(f"  ✓ nav written → {fn}")


if __name__ == "__main__":
    main()
