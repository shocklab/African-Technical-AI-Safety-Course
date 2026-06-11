# Open-source technical AI safety courses — research synthesis

Surveyed June 2026. The headline recommendation: use **Hendrycks' "Intro to ML Safety" as the
technical backbone** (correct prerequisite level, the only course with public coding psets), overlay
**BlueDot's Alignment spine** for current-frontier framing, clone **Grosse's Toronto course** for the
sequencing and the project rubric, and build the hands-on mech-interp/evals labs on **ARENA +
TransformerLens + UK AISI Inspect**.

> **Licensing reality check.** None of these post a clean blanket open licence. BlueDot is
> permissionless-with-attribution but doesn't own its linked third-party readings. CAIS materials are
> freely viewable, no explicit reuse licence (the AISES textbook's arXiv version, 2411.01042, is the
> cleanest to redistribute). ARENA requires a permission form + attribution for organisational use.
> **TransformerLens is MIT** (the one cleanly reusable codebase). Treat slides as "viewable, attribute,
> ask before redistributing"; assign readings by link rather than rehosting.

---

## The technical backbone & spines

### Hendrycks / CAIS — "Intro to ML Safety" ★ technical backbone
`https://course.mlsafety.org` · notes `https://github.com/centerforaisafety/Intro_to_ML_Safety`
23 lectures in 6 pillars, **advanced-undergrad/grad level, assumes ML/DL**. Public videos + slides +
some notes + **coding assignments** (adversarial robustness/PGD, anomaly detection, trojans, value
learning). Pillars: Safety Engineering (risk decomposition, accident models, black swans) → Robustness
→ Monitoring (anomaly detection, calibration, transparency, trojans, emergent behaviour/Goodhart) →
Control (honest models, power aversion, machine ethics) → Systemic Safety → X-Risk.
**Borrow:** the safety-engineering framing up front; the robustness/monitoring/control taxonomy; the
drop-in coding psets.

### BlueDot Impact — AI Safety Fundamentals ★ frontier-framing spine
`https://bluedot.org/courses` · reuse terms `https://blog.bluedot.org/p/running-versions-of-our-courses-2026`
The **Alignment** course's unit spine is the cleanest ready-made ordering for technical weeks:
1. AI & the years ahead · 2. What is alignment? · 3. RLHF (and AI feedback) · 4. Scalable oversight ·
5. Robustness, unlearning & control · 6. Mechanistic interpretability · 7. Technical governance ·
8. Contributing · 9–12. Project phase. The shorter **Technical AI Safety** course adds lab-by-lab
"Detecting Danger" deep-dives into real Anthropic/OpenAI/DeepMind/Meta safety frameworks & system cards.
The **Frontier AI Governance** course (6 units: read models like a policymaker → map power → stress-test
proposals → govern under pressure → take a side → roadmap) is the conceptual governance complement.
**Borrow:** the alignment unit ordering; the open facilitator/session guides; the system-card deep-dives.

### Grosse — CSC2547 "AI Alignment" (U. Toronto) ★ sequencing + project rubric
`https://alignment-w2024.notion.site/CSC2547-AI-Alignment-b44359978f3a4a8f95c90adb0a6e7d53`
12 lectures, the standout **two-act structure**: idealised agency (planning, AIXI/universal induction,
assistance games, cooperation) → empirical LLM alignment (RLHF, interpretability/superposition,
robustness, truthfulness, "whose values?"). Public annotated slides + tiered reading lists (core /
supplemental / **skeptical takes**). **Best assessment model to clone:** team proposal → NeurIPS-format
report + code, **per-section itemised rubric**, four project archetypes (incl. "test a lecture
speculation" and "build a novel toy example"), negative results explicitly welcome.

### Hendrycks — "AI Safety, Ethics, and Society" (textbook, free)
`https://www.aisafetybook.com/textbook` · arXiv **2411.01042**. Non-technical companion; **free online +
PDF + slides + audiobook**. Mathematically useful **appendices**: normative ethics, utility functions,
RL, long-tailed distributions, evolutionary game theory. **Borrow:** free assigned readings (Ch.1
catastrophic risks, Ch.2 fundamentals) + the appendices for maths-literate background.

---

## Hands-on labs (the coding spine)

### ARENA — Alignment Research Engineer Accelerator
`https://learn.arena.education/` · code `https://github.com/callummcdougall/ARENA_3.0` (permission
form + attribution for org use). Chapters: **0 Fundamentals** · **1 Transformer Interpretability**
(part 2 intro+induction heads; part 41 IOI/activation patching; part 33 SAEs; part 52 grokking/modular
arithmetic; part 54 superposition) · **2 RL** (intro→Q-learning/PG→PPO→RLHF) · **3 LLM Evals** (intro →
dataset gen → **running evals with Inspect** → LLM agents) · **4 Alignment Science** (emergent
misalignment, persona vectors, investigator agents). Every section is a Colab + web page + notebook +
`solutions.py`. **Use:** Ch.1 part2 (Session 14), part41 (Session 15), part33/52/54 (Session 16); Ch.2
RLHF (Session 6); Ch.3 Inspect (Session 11).

### Neel Nanda — mech-interp materials
**TransformerLens** `https://github.com/TransformerLensOrg/TransformerLens` (**MIT — cleanly reusable**);
glossary `https://neelnanda.io/glossary` (assign as reference); **"200 Concrete Open Problems in
Mechanistic Interpretability"** `https://www.lesswrong.com/s/yivyHaCAmMJ3CqSyj` + 12 released toy models
(a turnkey **project-idea bank**); YouTube paper walkthroughs (flipped-classroom pre-viewing).

### Stanford CS221M — Mechanistic Interpretability (lecture spine)
`https://cs221m.github.io/` (Icard, Geiger, et al., 2026). Causal-methods emphasis: LM review →
behavioural analysis/probes → causal interventions & steering → causal abstraction → automated
interpretability, then guest lectures + project. Public notebooks/slides on GitHub. **Borrow:** the
Weeks 2–5 lecture spine to complement ARENA's implementation focus. (Skip **Redwood MLAB** —
unmaintained since 2022, unlicensed, superseded by ARENA.)

---

## Evals & technical governance (Week 6 sources)

- **UK AISI Inspect** `https://inspect.aisi.org.uk/` · `https://github.com/UKGovernmentBEIS/inspect_ai` —
  `pip install inspect-ai`. Dataset/Solver/Scorer/Task abstractions; built-in **model-graded scorers**.
  `inspect_evals` has 200+ worked benchmark implementations. *The single highest-leverage classroom
  tool* — anchors the evals lecture, the LLM-as-judge lab, and project ideas 4–6.
- **METR** `https://evaluations.metr.org/` — public autonomy/dangerous-capability task suite + example
  protocol; lesson on elicitation/validity. Public task code `https://github.com/METR/public-tasks`.
- **Apollo Research** `https://www.apolloresearch.ai/` — in-context scheming / deception evals; setups
  simple enough to reproduce in miniature.
- **Frontier-safety frameworks:** Anthropic RSP · OpenAI Preparedness
  (`https://openai.com/global-affairs/our-approach-to-frontier-risk/`) · DeepMind FSF v3 · synthesis:
  METR "Common Elements of Frontier AI Safety Policies" (`https://metr.org/assets/common-elements-nov-2024.pdf`).
- **Technical AI governance field:** Reuel et al., "Open Problems in Technical AI Governance" (arXiv
  **2407.14981**, TMLR 2025) — *capacities* × *targets* taxonomy. Searchable project DB:
  `https://taig.stanford.edu/`.
- **LLM-as-a-judge biases:** survey arXiv **2411.15594** (position/verbosity/self-enhancement bias +
  mitigations) — pairs with the Inspect lab.

---

## Other university courses (for structure/assessment ideas)

- **Stanford CS120 "Intro to AI Safety"** (Lamparth) `https://web.stanford.edu/class/cs120/` — borrow
  the **anonymised peer-review-of-projects** component (~12%), unlimited-resubmission quizzes, and
  **three project tracks** (experimental / lit-review / policy) so non-empirical students aren't forced
  into experiments.
- **Princeton COS 597Q "AI Safety & Alignment"** (Hazan) `https://sites.google.com/view/cos598aisafety/` —
  borrow the dedicated **"criticisms of AI-risk narratives"** unit (feeds Session 20).
- **Berkeley CS294-166 "Foundations for Beneficial AI"** (Russell et al.)
  `https://people.eecs.berkeley.edu/~russell/classes/cs294/s20/announcement.html` — the **assistance-game /
  CIRL** formal unit as a maths-friendly theoretical anchor (pairs with the alignment-problem session).
- **Oxford AISAA** (Barez) `https://robots.ox.ac.uk/~fazl/aisaa/` — borrow the **"analyse one alignment
  failure mode" 1,500-word essay** as a low-stakes mid-course milestone.
- **MIT MAIA AISF-ML** `https://mitalignment.org/aisf-ml` — a curated reading list (non-credit reading
  group), derived from the BlueDot curriculum.

---

## Student project idea bank (~3–4 weeks, strong maths/Python students)

Sources: BlueDot alignment project ideas (`https://blog.bluedot.org/p/alignment-project-ideas`), Neel's
"200 Concrete Open Problems," Apart Research sprints (`https://apartresearch.com/sprints/all`), ARENA
capstones, TAIG DB. *The universal failure mode is over-scoping — pin a concrete deliverable + baseline
metric in week 1. API-only / pretrained-model designs are the safest guaranteed deliverables.*

**Interpretability** — 1) Linear-probe a concept across layers (very tractable). 2) SAE feature audit on
a small model with pretrained SAEs (low compute; fix model/layer up front). 3) Reproduce/extend a known
circuit (induction heads, IOI) with activation patching (canonical ARENA capstone).
**Evals** — 4) Build a model-graded Inspect eval for a narrow capability (reuses course tooling).
5) Quantify LLM-as-judge position/verbosity bias + test a mitigation (mostly API + stats — great maths
fit). 6) Author + human-baseline a new METR-spec autonomy task.
**Robustness** — 7) Adversarial probe of an open guardrail (attack success vs perturbation budget).
8) Stress-test machine unlearning (apply → attempt recovery). 9) Sandbagging detection via weight-noise
injection (hackathon-proven scope).
**Alignment-method replication** — 10) Weak-to-strong generalisation on an open model + tractable task
(watch compute). 11) Constitutional-AI mini-replication, critique stage only (cap scope).
**Conceptual / governance** — 12) Map a dangerous-capability framework (RSP/Preparedness/FSF) to a
concrete eval suite (analysis + light prototype). 13) Critically evaluate an AI Safety Institute, or
analyse open-weight release tradeoffs (pure conceptual track).

---

## One-line bottom line

Backbone = **Intro to ML Safety** (level + psets). Ordering + project rubric = **Grosse CSC2547**.
Frontier framing + facilitator guides = **BlueDot Alignment**. Labs = **ARENA + TransformerLens (MIT) +
UK AISI Inspect**. Free readings = **AISES textbook + appendices**. Differentiator = the **Global South
lens** carried from the sibling Gen-AI course.
