#!/usr/bin/env python3
"""Editorial restyle sweep for the lesson pages (docs/sessions/**/*.html).

Per page:
  1. drop the unused Brightspace Lato <link> (fonts now load via styles.css).
  2. h1: strip leading emoji, unwrap the white-on-blue <span>, sentence-case
     the title via H1MAP (acronyms/proper nouns protected by hand).
  3. strip every decorative emoji from the rest of the page (outside
     code/pre/script/style), keeping nav glyphs (<- -> home) and bullets.

Idempotent. Run:  python3 restyle_sweep.py        (apply)
                  python3 restyle_sweep.py --check  (report only)
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).parent / "docs" / "sessions"
CHECK = "--check" in sys.argv

# Exact h1 inner text (emoji + span removed, &amp; preserved) -> sentence-case.
H1MAP = {
    "Pace of Progress &amp; the Emergence Debate": "Pace of progress &amp; the emergence debate",
    "Technical AI Governance": "Technical AI governance",
    "Neural Scaling Laws": "Neural scaling laws",
    "Lab — From Base Model to Assistant": "Lab — from base model to assistant",
    "Inside the Transformer": "Inside the transformer",
    "Lab — Scaling Laws &amp; a First Look Inside a Model": "Lab — scaling laws &amp; a first look inside a model",
    "From Neurons to Networks": "From neurons to networks",
    "The Post-Training Stack &amp; Where Behaviour Is Shaped": "The post-training stack &amp; where behaviour is shaped",
    "From Predictor to Instruction-Follower": "From predictor to instruction-follower",
    "Infrastructure, Scale and the Rebound Problem": "Infrastructure, scale and the rebound problem",
    "Pretraining: Learning to Predict the Next Token": "Pretraining: learning to predict the next token",
    "Sustainable &amp; Sovereign AI": "Sustainable &amp; sovereign AI",
    "The Cost of Every Prompt": "The cost of every prompt",
    "Critical Minerals and the Hardware Supply Chain": "Critical minerals and the hardware supply chain",
    "The Optimizer's Curse": "The optimizer's curse",
    "Instrumental Convergence &amp; Power-Seeking": "Instrumental convergence &amp; power-seeking",
    "The Specification Problem": "The specification problem",
    "Deception, Corrigibility &amp; What We'd Even Know": "Deception, corrigibility &amp; what we'd even know",
    "Inner Alignment &amp; Goal Misgeneralisation": "Inner alignment &amp; goal misgeneralisation",
    "The Reward Model": "The reward model",
    "The Limits of RLHF": "The limits of RLHF",
    "From Demonstrations to Preferences": "From demonstrations to preferences",
    "Policy Optimisation: PPO &amp; the KL Leash": "Policy optimisation: PPO &amp; the KL leash",
    "Lab — Reward Models &amp; Over-optimisation": "Lab — reward models &amp; over-optimisation",
    "What Technical AI Safety Is (and Isn't)": "What technical AI safety is (and isn't)",
    "Safety Isn't Solved — Especially Not for Us": "Safety isn't solved — especially not for us",
    "The Case, and Its Strongest Critics": "The case, and its strongest critics",
    "How This Course Works": "How this course works",
    "Ubuntu, Relational Ethics &amp; the Just AI Framework": "Ubuntu, relational ethics &amp; the Just AI framework",
    "Whose Values? Preference Aggregation &amp; the Alignment Target": "Whose values? Preference aggregation &amp; the alignment target",
    "Scalable Oversight: The Supervision Gap": "Scalable oversight: the supervision gap",
    "Ethical Frameworks &amp; the Four Lenses": "Ethical frameworks &amp; the four lenses",
}

BRIGHTSPACE = re.compile(r'[ \t]*<link rel="stylesheet" href="https://s\.brightspace\.com/lib/fonts/0\.6\.1/fonts\.css">\n?')
PROTECT = re.compile(r'(<code\b[^>]*>.*?</code>|<pre\b[^>]*>.*?</pre>|<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>)', re.S)
SWALLOW = ' ‍️⃣'  # space, ZWJ, variation selector, combining keycap


def is_emoji(ch):
    o = ord(ch)
    if o in (0x2190, 0x2192, 0x2302):  # keep nav glyphs <-  ->  home
        return False
    if o in (0x21AA, 0x21A9):          # strip the curly "next/back" arrows
        return True
    return (0x1F000 <= o <= 0x1FAFF or 0x2600 <= o <= 0x27BF or 0x2300 <= o <= 0x23FF
            or 0x2B00 <= o <= 0x2BFF or 0xFE00 <= o <= 0xFE0F or o in (0x2705, 0x274C, 0x2764, 0x2B50))


def strip_emoji_text(s):
    out, i, n = [], 0, 0
    while i < len(s):
        if is_emoji(s[i]):
            i += 1; n += 1
            while i < len(s) and s[i] in SWALLOW:
                i += 1
            continue
        out.append(s[i]); i += 1
    return ''.join(out), n


def strip_emoji_doc(t):
    parts = PROTECT.split(t)
    total = 0
    for k, p in enumerate(parts):
        if p.startswith('<code') or p.startswith('<pre') or p.startswith('<script') or p.startswith('<style'):
            continue
        parts[k], n = strip_emoji_text(p)
        total += n
    return ''.join(parts), total


unmapped = []

def fix_h1(m):
    inner, _ = strip_emoji_text(m.group(1))
    inner = inner.strip()
    sm = re.match(r'^<span style="color:#ffffff;">(.*?)</span>$', inner)
    text = sm.group(1) if sm else inner
    if text not in H1MAP:
        unmapped.append(text)
    return '<h1>' + H1MAP.get(text, text) + '</h1>'


def main():
    files = sorted(ROOT.rglob("*.html"))
    changed = 0
    emoji_removed = 0
    bs_removed = 0
    for f in files:
        t = orig = f.read_text(encoding="utf-8")
        t, nb = BRIGHTSPACE.subn('', t); bs_removed += nb
        t = re.sub(r'<h1[^>]*>(.*?)</h1>', fix_h1, t, flags=re.S)
        t, ne = strip_emoji_doc(t); emoji_removed += ne
        if t != orig:
            changed += 1
            if not CHECK:
                f.write_text(t, encoding="utf-8")
    print(f"{'(check) ' if CHECK else ''}files changed: {changed}/{len(files)}")
    print(f"emoji removed: {emoji_removed} ; brightspace links removed: {bs_removed}")
    if unmapped:
        print("\n!! h1 titles NOT in H1MAP (add them):")
        for u in sorted(set(unmapped)):
            print("   -", u)
    else:
        print("all h1 titles mapped to sentence case ✓")


if __name__ == "__main__":
    main()
