# Writing conventions — words and structures to avoid

The course grades students on thinking clearly and checking claims against sources. The prose
should model that. These are the AI-writing tells we have actually overused, measured across the
built pages on 2026-06-25 (counts are visible-text occurrences across 68 pages). This file is the
course-specific layer; the global canon at `~/.claude/writing-tells.md` still applies underneath it.

The fix is almost always **subtraction**: cut the word, keep the sentence. If a flagged word is the
right word, keep it — this is a prior, not a ban.

---

## 1. The dominant tell: telling the reader how to feel about the point

This is the one that matters most, and it subsumes half the word-list below. We keep labelling our
own points as important, clean, strongest, cleanest, the lesson, the headline — instead of stating
the thing and trusting the reader to judge its weight.

Real examples from the pages, all to be cut:
- "the single cleanest epistemics unit in the block"
- "the high-water mark of the evidence"
- "the arc is the lesson", "the pairing is exactly the calibrated epistemics the course is built on"
- "worth teaching exactly", "the line to put on the slide"
- "load-bearing" (claims, admissions, papers), "the headline", "the punchline", "the point is",
  "the move", "the prize", "the catch"

**Rule:** state the claim; delete the label. The reader decides what is load-bearing.

Also in this family — **pedagogical meta-commentary** that narrates the teaching rather than teaching:
"we teach this as…", "the lesson to take away is…", "hold that thought", "in one sentence", "notice
that". Cut the frame, keep the content.

## 2. Contrastive reframes (a structure, not a word)

"not just X but Y" (34), "not merely X" (6), "it's not X, it's Y", "X isn't Y; it's Z". Forty-odd of
these. Rewrite as a direct statement: *"not just a benchmark but a commitment device"* → *"a
commitment device, not only a benchmark"* — or better, just say what it is.

## 3. Intensifier filler — cut on sight unless literal

| word | count | keep only when… |
|---|---|---|
| exactly | 113 | literal ("exactly one fixed point") |
| genuine / genuinely | 76 | (almost never — delete) |
| precisely | 47 | literal ("precisely when λ = 0") |
| the whole | 68 | literal ("the whole matrix", "the whole training set") |
| worth (…ing) | 35 | rarely; "worth teaching" is usually meta — cut |
| truly, really, simply, just, actually | — | delete |

Default: delete and the sentence is stronger.

## 4. "honest" / "honestly" — the ethos word, used 139 times

Keep it where it names the course's epistemic stance as a concept — "the honest limits of
interpretability", "honest epistemics", the honesty box. Cut the reflexive adverb ("it is honestly a
modest one" → "it is a modest one") and the filler adjective ("the genuine, honest traction"). Aim to
roughly halve it.

## 5. Essayist tics — replace with plain words

`lands` (figurative), `rhymes with`, `cash out / cashes out`, `earn(s) its keep`, `the spine / spine
of`, `the wedge`, `the through-line`, `tee up`, `reckoning` ("honest reckoning" → "honest account"),
`the uncomfortable X`, `a clean X` / "clean demonstration" (vary it — "clean" appears 22 times),
`vivid`, `hold that / hold onto / carry that`, `in one sentence / in one line / in a word`.

## 6. The global canon still applies

Everything in `~/.claude/writing-tells.md`: delve, leverage, harness, underscore, bolster, foster,
robust (figurative), comprehensive, seamless, intricate, nuanced, multifaceted, holistic, pivotal,
groundbreaking, transformative, testament, realm / landscape (figurative); connective-adverb stacking
(Moreover, Furthermore, Additionally, Ultimately); pseudo-depth openers (At its core, In essence,
Fundamentally); participle fake-depth (…ing clauses bolted on for weight: "highlighting its
importance", "underscoring the significance"); significance adverbs (crucially, notably, importantly,
tellingly); rule-of-three padding; em-dash ≤ 1 per paragraph (or one genuine — paired — parenthetical);
sentence-case headings; no decorative emoji.

## 7. Keep — legitimate terms that look like tells

- **robustness / robust** — the field's name for the Session 9 subject and the adversarial-ML property.
  Keep as the technical term; avoid only the figurative "robust evidence" (→ "strong").
- **honest / honesty** — as the course's named stance, used sparingly (see §4).
- **by construction** — legitimate maths phrasing where literally true.
- **necessary but not sufficient** — standard logic phrase.
- **superposition, circuit, feature, induction head, residual stream, …** — technical vocabulary;
  never "vary for elegance". Use the reader's term and reuse it.
- **"drops sharply"** and other literal uses of `sharp` — fine. Cut only "the sharpest version of the
  argument" and similar.

## 8. How to apply it

Surgical edits: change the flagged word or phrase, not the surrounding sentence. Never touch text
inside HTML tags, inside MathJax (`\(…\)`, `\[…\]`), or inside code. Preserve every citation, number,
and technical claim verbatim. Don't introduce a new tell while removing an old one. After a pass,
re-run the count script and the em-dash / banned-word scan and confirm the numbers fell.
