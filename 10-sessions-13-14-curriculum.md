# Sessions 13–14 — Interpretability foundations (+ induction-head lab)

**Week 7, Part IV (Mechanistic interpretability).** Status: curriculum drafted 2026-06-25 from a survey
of existing courses (ARENA, the Transformer Circuits thread, Neel Nanda/TransformerLens, Distill) +
literature **verified against the actual papers** (see source log). Awaiting sign-off before building HTML.

## Where it sits, and the gap it fills

Sessions 13–16 open the black box. Session 13 is the foundations: what a *feature* and a *circuit* are,
why **superposition** makes naive interpretation fail, and how attention heads decompose into **QK/OV**
circuits that compose into algorithms — with **induction heads** as the worked flagship. Session 14 is
the hands-on lab: load a small model in TransformerLens, find an induction head, and verify it causally
by ablation. The gap a maths-honest course fills: ARENA teaches interp as a coding bootcamp (the linear
algebra is implicit) and the Transformer Circuits papers bury the maths in research prose. Our students
own linear algebra and the transformer forward pass (S2.2), so we *derive* QK/OV as low-rank bilinear
forms, treat "features as directions" as a falsifiable linear-representation hypothesis with the
Johnson–Lindenstrauss count behind superposition explicit, and present induction heads as a composed,
writable algorithm.

**Coherence guardrails (reference, do not re-derive):**
- S2.2 "Inside the transformer": attention, MLPs, residual stream, multi-head — *assumed*. S13.3 reframes them in interp language (additive paths, QK/OV); it must not re-teach the forward pass.
- S11.1 already defines internal/white-box vs behavioural/black-box evals — S13.1 cites that and slots interp into it.
- Safety *applications* and *limits* of interp are **Session 16's** job — S13 motivates and forward-points only. RepE / circuit breakers (Zou 2406.04313) already appeared in S10 — reference, don't re-cover.
- Distill *Zoom In* is CNN-vision — use it for the features/circuits/universality *vocabulary* only.

## Session 13 — structure (4 expository sub-sessions)

### 13.1 — Why open the black box? Interpretability as the white-box toolkit
Define mechanistic interp vs saliency/probing vs black-box evals; slot it into S11.1's white-box/black-box frame; the reverse-engineering ambition and its honest epistemic status (clean for 1–2-layer attention-only models, "more like neuroscience" at frontier scale — Olsson et al.'s own framing). Forward-point (one sentence each) to S12 audit/access and S16. **Worked:** a "levels of explanation" contrast on one behaviour (black-box → attribution → mechanistic).
- Readings: Olah et al. *Zoom In* (Distill 2020); Olsson et al. `2209.11895` §1.

### 13.2 — Features, directions, and the superposition problem
Linear representation hypothesis (decomposability + linearity); privileged vs non-privileged basis (why "is this *neuron* interpretable?" only makes sense in a privileged basis); superposition (more features than dimensions via almost-orthogonal directions); sparsity as the driver; superposition → polysemanticity → why you can't just read neurons. **Worked (load-bearing):** (a) the Johnson–Lindenstrauss almost-orthogonal count — \(n\) orthogonal vs \(\exp(\Theta(\varepsilon^2 n))\) near-orthogonal directions; (b) the closed-form 2-features-in-1-dimension toy model with its **first-order phase change** as sparsity rises (the rare interp result with a clean closed form).
- Readings: Elhage et al. *Toy Models of Superposition* `2209.10652` (Definitions & Motivation; Superposition as a Phase Change).

### 13.3 — The circuits paradigm: residual stream, QK/OV, heads as functions
Residual stream as a communication channel (everything reads/writes subspaces by addition → logits decompose into a sum over paths); attention head effect splits into **QK** (where it attends) and **OV** (what it writes); 1-layer attn-only = bigram + skip-trigram (no composition); composition (Q/K/V) is what depth-2 buys. **Worked:** derive the bilinear forms — attention score \(x_i^\top W_Q^\top W_K x_j\), define \(W_{QK}:=W_Q^\top W_K\) (low-rank), show the \(W_Q,W_K\)-product invariance (only the product matters); output \(W_{OV}:=W_O W_V\); sketch the path expansion so the induction term is visible before 13.4 names it.
- Readings: Elhage et al. *A Mathematical Framework for Transformer Circuits* (transformer-circuits.pub, 2021) — residual stream, QK/OV, one- vs two-layer.

### 13.4 — Induction heads & in-context learning (the worked flagship)
Behaviour (complete `[A][B]…[A]→[B]`); mechanism (layer-0 previous-token head + later induction head via **K-composition**, then OV-copy); why two layers are necessary; the induction-head → in-context-learning hypothesis with its evidence **honestly graded** (causal for small attn-only models via >50k ablations; correlational at scale); the training-time **phase change** (loss bump co-occurring with an ICL-score jump); fuzzy matching incl. word-by-word translation (bridge to the African angle). **Worked:** OV-copying ⇔ positive eigenvalues; QK prefix-matching via K-composition; define the **prefix-matching score** and **copying score** (the two detectors the S14 lab implements).
- Readings: Olsson et al. `2209.11895` (Induction Heads; phase-change + ablation arguments). *Optional flagship 2:* Nanda et al. grokking/modular-addition `2301.05217` (the only fully closed-form circuit; pairs with 13.2's phase change).

## Session 14 — Lab: find & verify an induction head (TransformerLens)
**CPU-friendly** (forward passes + ablation only, no training; gpt2-small runs on CPU). Core: (1) load + cache; (2) plot attention on a repeated-random-token sequence, see the "induction stripe"; (3) find the layer-0 previous-token head; (4) implement the **induction score** (and optionally copying score) to rank heads; (5) **causally verify** by ablating the induction head and the prev-token head and measuring the loss rise (reproduces Olsson et al.'s ablation argument at toy scale). Stretch: logit attribution; 1-layer-vs-2-layer contrast (induction *absent* in 1 layer); inspect the induction head's \(W_{OV}\) eigenvalues. **Models:** gpt2-small (real model) + attn-only-2l (clean maths). **Pin the TransformerLens version** (3.x deprecates `from_pretrained` in favour of `TransformerBridge`) so the notebook doesn't rot.

## African-lens / sovereignty angle (honestly thinner — say so)
Interp's African angle is genuinely thinner than robustness/evals; the course principle is not to fake one. Two genuine angles: **(A, strong)** interpretability is the toolkit for *auditing a model you did not train* — it works on the artefact (weights) without the developer's data or cooperation, so it is the sovereign deployer's only route from "what does this imported model do on my tests" to "why" (ties to S12 audit/access). State honestly that this is currently an aspiration at frontier scale. **(B, open question)** are features/circuits language-specific? Olsson et al.'s translation induction head suggests some circuits are language-agnostic; if key features for low-resource languages sit disproportionately in superposition, that is a concrete, testable, locally-relevant research question (project seed). Flag plainly that foundational interp maths is geography-neutral.

## Verified reading list (full-text-checked 2026-06-25)
Elhage et al. *Mathematical Framework* (transformer-circuits.pub 2021) — residual stream, QK/OV low-rank, heads additive, 1-layer=bigram+skip-trigram, 2-layer=composition=induction · Olsson et al. `2209.11895` — induction = prefix-match + copy; two-head K-composition circuit; needs ≥2 layers; phase change (loss bump + ICL-score jump); >50k ablations causal for small models, correlational at scale; fuzzy/translation matching; **post-publication erratum to the prefix-match definition** (a teachable honesty moment) · Elhage et al. *Toy Models of Superposition* `2209.10652` — feature=direction; superposition via almost-orthogonal directions; sparsity drives it; first-order phase change (analytic in the toy-of-toy model); geometric structures (digon/triangle/pentagon) · Olah et al. *Zoom In* (Distill 2020) — features/circuits/universality vocabulary (CNN-vision) · Nanda et al. `2301.05217` — modular-addition Fourier-multiplication circuit + progress measures (optional).

## Source-verification log (2026-06-25)
Research agent checked all five against full paper text. All load-bearing claims above confirmed (QK/OV factorisation, induction-head mechanism + phase change + evidence grading, the superposition phase change and JL count, the grokking algorithm). TransformerLens CPU-feasibility + `run_with_cache`/hook-ablation idioms confirmed against the repo.

## Open choices for sign-off
1. **Maths depth:** three derivations (QK/OV invariance; superposition closed-form phase change; OV-copying + K-composition) — *recommended*, matches the textbook-depth standard — or trim to one (the superposition closed form) with the others as stated results.
2. **One flagship circuit or two:** induction heads core, with Nanda's grokking as *optional* reading — *recommended* — vs promoting grokking to a second core circuit (risks bloating the session).
3. **Lab models + version:** gpt2-small + attn-only-2l, TransformerLens pinned to a specific version/API — *recommended* — vs attn-only-2l only (simpler, loses the "survives in a real model" payoff).
