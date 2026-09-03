# CLAUDE.md — African Technical AI Safety course

Working notes for Claude Code sessions on this repo. The course is a static
GitHub Pages site served from `docs/` on `main`
(https://shocklab.github.io/African-Technical-AI-Safety-Course/).

## Writing style — load-bearing

The course prose must read as human-written, not machine-generated. The global
`human-prose` output style applies, and on top of it:

- **Run the `writing-review` skill on any prose you write or substantially edit,
  and apply its fixes, before committing/publishing.** This is a standing step,
  not optional — it audits for AI-writing tells ("Claude-isms") and de-Claudifies.
  Applies to lesson pages, the contents page, and any user-facing copy.
- Workflow: after drafting/editing a page's prose, invoke `writing-review` on that
  page, apply the fixes, then commit. For a batch of pages, review each before the
  batch is pushed.
- The catalogue of tells is at `~/.claude/writing-tells.md`. **The course-specific layer is
  `STYLE.md` at this repo root — read it before writing or sweeping any prose here.** It carries
  the heading families, the per-1,000-word density budgets with this course's measured numbers,
  the protect-lists (terms of art like "angle", model-honesty subject matter, the named
  through-lines), the title-layer rules (three zones agree; "and" over "&"; full titles on the
  contents page), and §11's authoring-time rules for new pages and agent briefs.

## House visual style — editorial (do not regress)

- Flat editorial design in `docs/assets/styles.css`: Fraunces (display headings),
  Source Serif 4 (body), IBM Plex Mono (labels); UCT blue `#003A70` / `#2a5298`.
- **No decorative emoji** anywhere (the nav glyphs ← → ⌂ and list bullets are fine).
- Page titles in **sentence case** as a plain `<h1>Title</h1>` (no white-on-blue
  `<span>`, no leading icon).
- New pages inherit all type/scale from `styles.css`. Do not reintroduce the old
  rounded-card / drop-shadow / gradient-header look or emoji headings.
- `restyle_sweep.py` re-applies the emoji strip + sentence-case if anything slips in.

## Publishing discipline

- Every reading is a working, verified link. `linkify_readings.py` holds the
  verified URL map and auto-links arXiv IDs; verify any new reference resolves and
  points to the correct work before publishing, and log it in `05-reading-lists.md`.
- After adding/reordering pages: run `python3 add_page_nav.py` (prev/next nav) and
  `python3 add_mathjax.py` (MathJax loader). Write maths as `\(…\)` / `\[…\]` —
  never single `$` — and keep code / arXiv IDs / filenames in `<code>`.
- **Branch discipline (since 2026-07-18): the site is GATED.** Public `main` shows only released
  sessions (`RELEASED-SESSIONS` at the root); the **`dev` branch holds the full course** and is
  where ALL content edits go (private remote `dev-origin`, repo
  `African-Technical-AI-Safety-Course-dev`; Ben Sturgeon is a collaborator there). To publish:
  `python3 tools/release.py N` (new week) or `python3 tools/release.py sync` (revisions to
  released weeks), review, then push `main` to BOTH remotes. **Never hand-edit `docs/index.html`
  on `main`** (regenerated per release), and **never force `dev` to `main`** — that destroys the
  full course. Repo-level files (STYLE.md, tools/, this file's tracked siblings) change on `main`
  and get cherry-picked onto `dev`. GitHub Pages redeploys in ~30s after a push to `main`.
- **Preview site (unadvertised, for Ben):** the FULL course is live at
  https://shocklab.github.io/African-Technical-AI-Safety-Course-preview/ — a public repo
  (`…-Course-preview`, remote `preview`) that is linked from nowhere and carries a
  noindex robots.txt (which lives on dev only; never add it to release.py's SYNC_PATHS —
  the gated public site must stay indexable). **After any push to dev, also run
  `git push preview dev:main`** to keep the preview current. The durable dev checkout is
  `/Users/jonathanshock/Cursor folders/ATAS-dev-full-course`.
