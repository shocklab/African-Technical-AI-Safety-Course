# Session 9 — Robustness & adversarial ML

**Week 5, Session 1** (Session 10 is the second). Status: curriculum drafted 2026-06-25 from a
survey of existing courses + literature **verified against the actual papers** (see source log).
Awaiting sign-off before building HTML.

## Where it sits, and the gap it fills

Session 1 opened with the course's anchor — Yong et al.'s low-resource-language jailbreak. Session 9
is where that result stops being a reading and becomes a **controlled experiment the students run by
hand**. The session treats a jailbreak as an *optimisation problem*, explains *why* safety training
must fail off-distribution (not just that it does), and ends honest about robustness being an unsolved
arms race with a distributional-justice edge. The survey showed no existing course (ARENA, BlueDot,
Hendrycks AISES, the Madry/Kolter adversarial-ML lineage) offers a hands-on low-resource-language
robustness lab — that is ours.

**Coherence guardrails (reference, do not re-derive):**
- S1 (Yong anchor): operationalise it as the 9.4 lab; one callback sentence, then build.
- S3 (deception/power-seeking): adversarial robustness is the *misuse/external* axis; at most one line linking "safety habit fails OOD" to goal misgeneralisation.
- S6 (RLHF): may *cite* the KL-to-base + pretraining terms to locate the competing-objectives trade-off; do not re-derive RLHF.
- S7 (RLAIF/CAI): mention only as a candidate mitigation / project direction (does constitutional training narrow the isiZulu gap?).
- S8.1 (oversight): red-teaming here *finds* failures, it does not *supervise* training — keep debate/amplification/sandwiching in S8.
- S10 (unlearning/control) and S11 (dangerous-capability evals): forward-point; defences here stop at adversarial training / certification / filtering; the 9.4 lab measures a *refusal/robustness* property, not a capability benchmark.
- S12 (governance): "robustness is an unsolved arms race with a distributional-justice dimension" is the hand-off; state, don't develop.

## Session-level learning objectives

By the end a student can: (1) define an adversarial example and a threat model precisely, and derive FGSM; (2) read the GCG algorithm line-by-line and state a jailbreak as discrete optimisation; (3) explain Wei et al.'s two failure modes (competing objectives; mismatched generalisation) and why scaling won't fix them; (4) measure English-vs-isiZulu refusal degradation with confidence intervals, and reason about the translation-quality confound; (5) describe indirect prompt injection and data poisoning, and give the honest state of defences.

## Proposed structure — 5 sub-sessions (4 expository + 1 lab)

### 9.1 — From pandas to prompts: what an adversarial example is
Szegedy's discovery → Goodfellow's linear hypothesis; threat-model vocabulary (white/black-box, perturbation set, targeted/untargeted, transfer). **Worked:** derive FGSM from a first-order Taylor expansion under an \(L_\infty\) ball (\(\eta=\varepsilon\,\mathrm{sign}(\nabla_x J)\)); the panda→gibbon \(\varepsilon{=}0.007\), 99.3% example. **African hook:** the perturbation that matters for African deployment is a *change of language*, not an \(L_\infty\) pixel ball.
- Readings: Goodfellow et al. `1412.6572`; Hendrycks AISES §3.3 (framing).

### 9.2 — Jailbreaks as optimisation: GCG and the discrete-search problem
Manual jailbreaks → automated suffix search; the affirmative-prefix trick; GCG Algorithm 1 (one-hot embedding gradient → top-k → exact forward-pass select). **Worked:** write the objective \(\min -\log p(\text{target prefix}\mid \text{prompt}\oplus\text{suffix})\); read the results table (Vicuna 88/99–100%; transfer GPT-4 46.9% vs Claude-2 2.1%) *with* the distillation caveat (Vicuna is distilled from ChatGPT, inflating GPT transfer). **African hook:** GCG is optimised on English tokenisers; isiZulu morphology/tokeniser fragmentation as an attack-surface variable.
- Readings: Zou et al. (GCG) `2307.15043` §2 + Tables 1–2.

### 9.3 — Why safety training fails: competing objectives & mismatched generalisation
Wei et al.'s two modes; prefix injection / refusal suppression vs Base64/cipher/**translation**; why scaling won't fix it (the KL-to-base term guarantees the safety/pretraining trade-off — ties to S6); capabilities that emerge with scale (GPT-4 follows Base64, GPT-3.5 can't). **Worked (conceptual):** write the RLHF objective schematically and show *where* the competing objective lives. **African hook:** quote the paper's own caution on cross-lingual generalisation; state the hypothesis the 9.4 lab tests.
- Readings: Wei, Haghtalab & Steinhardt (Jailbroken) `2307.02483`.

### 9.4 — Lab (flagship): measuring safety degradation in isiZulu, by hand
Run the S1 anchor as a controlled experiment. **Ethics frame first** (refusal-rate measurement, not capability elicitation; mild refusable prompt set; BAD/GOOD/UNCLEAR labelling at the refusal boundary). Procedure: English baseline refusal rate → translate to isiZulu (+ optional higher-resource African contrast) with a *logged, back-translated* pipeline → refusal rate per language → degradation Δ + bootstrap CI → refusal-vs-resource scatter. **Worked:** hand-computed rates with CIs; inter-rater agreement (Cohen's κ). Project seed for S13/S18.
- Readings: Yong et al. `2310.02446` (now a method to reproduce); Wei et al. §4 (labelling scheme).

### 9.5 — Indirect injection, poisoning, and the honest state of defences
Indirect prompt injection (Greshake: retrieval/agents dissolve the data/instruction boundary; Bing/Copilot demos; prompts-as-worms); data poisoning (one beat: web-scale poisoning is cheap; backdoors survive instruction tuning); red-teaming as defence (Perez/Ganguli; offence-defence asymmetry); defences and limits (adversarial training min-max; randomized-smoothing certified radius; filtering just moves the attack). **Honest verdict (verified from the GCG paper):** the best robustness methods are almost never deployed — too costly, hurt clean accuracy, narrow threat models. **Worked:** state \(\min_\theta \mathbb{E}[\max_{\|\delta\|\le\varepsilon} L]\) and the certified-radius idea; interpret, don't implement. **African hook:** indirect injection via local content ecosystems; defences are compute/annotator-expensive exactly where languages are lowest-resource.
- Readings: Greshake et al. `2302.12173`; Perez et al. `2202.03286`; pointers to Madry `1706.06083`, Cohen et al. `1902.02918`, a poisoning paper (open choice).

## Verified reading list (full-text-checked 2026-06-25 unless noted)

**Core:** Goodfellow et al. `1412.6572` (FGSM; linear hypothesis; ε=.007 panda→gibbon 99.3%; adv. training MNIST adv-error 89.4→17.9%) · Zou et al. `2307.15043` (GCG Alg.1; Vicuna 88%/99–100%, Llama-2 57/88%; transfer GPT-3.5 86.6, GPT-4 46.9, Claude-2 2.1; distillation caveat) · Wei et al. `2307.02483` (competing objectives + mismatched generalisation; combination attacks >96%; held-out combination_3 0.93 GPT-4 / 0.87 Claude; verbatim cross-lingual-caution line) · Yong et al. `2310.02446` (S1 anchor; EN <1% → 79% combined, isiZulu 53%) · Greshake et al. `2302.12173` (indirect prompt injection; Bing/Copilot; threat taxonomy; demonstration paper) · Perez et al. `2202.03286` (LM red-teaming; 3.7% zero-shot → >40% with RL on Gopher; data leakage/PII findings).
**Supplementary (cite one idea each; not all full-text-verified — see open choices):** Ganguli et al. `2209.07858` (human red-team release) · Madry et al. `1706.06083` (PGD min-max) · Cohen et al. `1902.02918` (randomized smoothing) · a poisoning paper: Carlini et al. `2302.10149` *or* Wallace et al. `2305.00944`.

## Source-verification log (2026-06-25)
Core six checked against full PDF text (research agent, `answer_pdf_queries`): all headline numbers above confirmed. The Wei et al. cross-lingual-caution sentence is verbatim and is the theoretical bridge to the 9.4 lab. **To verify before build:** the chosen poisoning exemplar; Ganguli `2209.07858` if promoted from "cite" to a reading.

## Open choices for sign-off
1. **Poisoning exemplar (9.5):** Carlini `2302.10149` (supply-chain/economics framing — *recommended*, links to S4 data-economics) vs Wallace `2305.00944` (instruction-tuning backdoors). Verify the chosen one before build.
2. **Lab posture (9.4):** model (open-weights *recommended* — controllable, ToS-safe — vs API), prompt set (mild refusal-eliciting *recommended*), languages (isiZulu + a higher-resource African contrast like Afrikaans/Yoruba to show the *gradient* — *recommended*).
3. **Maths depth (9.1–9.2):** keep full FGSM derivation + full GCG Algorithm-1 walkthrough (*recommended*, matches textbook-depth standard) and trim 9.5 defences to *stated* objectives.
