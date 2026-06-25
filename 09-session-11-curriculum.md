# Session 11 — Evaluations & dangerous-capability evals

**Week 6, Session 1** (Session 12, governance, is the second and is already built). Status: curriculum
drafted 2026-06-25 from a survey of existing courses + literature **verified against the actual papers**
(see source log). Awaiting sign-off.

## Where it sits, and the gap it fills

This session owns **the science of evaluation**: what it means to measure a capability or a propensity,
how the field builds dangerous-capability evals, and — the part a maths course is uniquely placed to
teach — **how to know whether the number is real**. Error bars, construct validity, and elicitation are
the three places a confident-looking eval can quietly be lying. S12 already owns the eval→governance
chain (RSPs, compute thresholds, Reuel taxonomy); S11 hands it a clean baton. The course's promised
"evaluation project on open African-language data" lands in the 11.5 lab.

One-line thesis: *every other group answers "what should we measure?"; a maths-honest course also
answers "and how do we know the number is real?"*

**Coherence guardrails (reference, do not re-derive):**
- S2.4 (metric mirage, Schaeffer): reuse as the bridge into construct validity (11.3); re-anchor in one line, don't re-derive emergence.
- S8.1 (oversight): when 11.1 mentions evaluating what humans can't check, point to S8.1; don't reopen oversight.
- S9 (robustness/red-teaming): **boundary** — S11 frames red-teaming as one *elicitation* method and owns sandbagging/eval-awareness (eval-integrity); S9 owns red-teaming as attack methodology. (Open choice C.)
- S12 (governance): the whole eval→commitment→threshold→RSP/FSF chain lives in S12; state the theory-of-change in *one slide* in 11.1 and hand off.
- S1 (isiZulu anchor): delivered on in 11.5; reference explicitly. S18 (Global South): 11.5's artifact is the project seed.

## Session-level learning objectives

By the end a student can: (1) state why evaluation is load-bearing for safety and hold the four distinctions (capability vs propensity; behavioural vs internal; static vs agentic; upper- vs lower-bound); (2) explain how a dangerous-capability battery is built, why elicitation makes a capability eval an upper bound, and what sandbagging does to that logic; (3) apply construct/measurement validity to "reasoning"/"agentic capability"/"dangerous knowledge" and see how the metric can manufacture the finding; (4) put error bars on an eval — binomial/clustered CIs, paired-difference tests, power — and judge when a leaderboard gap is real; (5) build a small in-language safety eval end-to-end, score it honestly, and name its confounds.

## Proposed structure — 5 sub-sessions (4 expository + 1 lab)

### 11.1 — Why evaluate, and a taxonomy of evals
The Shevlane et al. framing — **dangerous-capability** evals ("is it capable of extreme harm?") vs **alignment/propensity** evals ("does it have the propensity to apply them?"). Four distinctions held cleanly; map the org ecosystem (METR/AISI = capability+agentic; Apollo = propensity+white-box) onto them. The eval→risk→decision theory of change in *one slide*, handed to S12. **Worked:** a 2×2 (capability/propensity × behavioural/internal) sorting exercise — place WMDP, AgentHarm, the Apollo scheming suite, a linear deception probe, an isiZulu refusal eval. **African hook:** an eval is only evidence about the *distribution it samples* — and almost every frontier eval samples English only.
- Readings: Shevlane et al. `2305.15324` (core); skim Casper et al. `2401.14446` (access taxonomy).

### 11.2 — Dangerous-capability evals: domains, elicitation, sandbagging
Phuong et al. (GDM): four piloted domains (persuasion/deception, cyber, self-proliferation, self-reasoning; CBRN preliminary), scaffolded models, no safety filters; verified headline "**no evidence of strong dangerous capabilities… but early warning signs**." Elicitation as a *bias* argument (under-elicitation biases toward "safe" — the dangerous error direction). Sandbagging (van der Weij: prompt/password-lock; target-accuracy calibration) and Apollo's in-context scheming suite (Meinke: o1 schemes across all six evals, maintains deception >85% of follow-ups; gpt-4o none). The trichotomy: a passed safety eval = genuinely safe **or** badly elicited **or** sandbagged — distinguishing them needs white-box access. **Worked:** elicitation-gap arithmetic (p₀ zero-shot → p₁ scaffolded → p₂ fine-tuned; why the *max* is the conservative estimate; E[measured] ≤ true under weak elicitation). **African hook:** elicitation is language-dependent — prompting in English about an isiZulu-context task under-elicits and looks falsely safe; the elicitation gap and the language gap are the same measurement error.
- Readings: Phuong et al. `2403.13793` (skim tables); van der Weij et al. `2406.07358` (defn + Table 1); Meinke et al. `2412.04984` (intro + six-eval taxonomy).

### 11.3 — Does the eval measure what it claims? Construct & measurement validity
Import psychometric vocabulary (content/construct/criterion validity; reliability). Raji/Bender's "everything in the whole wide world" critique as the spine; the Schaeffer echo (the metric generates the claim — reused from S2.4). The concrete construct question: **WMDP measures hazardous-knowledge recall — is that a valid proxy for uplift to build a weapon?** Reliability/variance: an eval is a random variable across prompt phrasing, few-shot order, seed, scorer. **Worked:** the metric flips the verdict — score the same outputs exact-match (discontinuous) vs token-edit-distance (continuous); one shows an "emergent jump," the other a smooth curve; articulate which claim each licenses. **African hook:** construct validity *is* the representativeness problem — an "English understanding" benchmark sold as "language understanding" is the Grover-museum move, and it is what makes English-only safety evaluation miss isiZulu failures.
- Readings: Raji et al. `2111.15366` (core); Schaeffer et al. `2304.15004` (re-anchor only).

### 11.4 — The statistics of evals: error bars, comparisons, time horizons
Miller's *Adding Error Bars to Evals* as the backbone: pass rate as binomial/cluster sample; SEM + CLT 95% CI; **clustered SEs** when questions group (can be >3× naive); **paired-difference tests** exploiting cross-model question correlation; **power analysis** before running; multiple-comparison/winner's-curse on leaderboards. METR's time horizon as the integrative case: logistic fit of success vs human task-time, the 50% threshold as a *derived* quantity with uncertainty, hierarchical bootstrap, external-validity caveat. **Worked (maths spine):** (a) 43/50 passes → rate + normal-approx 95% CI (note Wilson); does it overlap a second model at 0.78? (b) two models on the *same* 50 questions, ρ≈0.5 → paired-test CI far tighter than independent (independent comparison can wrongly call a real gap insignificant); (c) one-line power calc for a 3pp difference at 80%. **African hook:** small African-language eval sets → wide CIs, so honest error bars are what separate a real in-language safety gap from sampling noise.
- Readings: Miller `2411.00640` (core; Anthropic write-up as on-ramp); METR `2503.14499` (blog + method).

### 11.5 — Lab: build a refusal/robustness eval on open isiZulu data (the project seed)
A controlled, open-model replication of Yong et al. **Pipeline:** (1) a *capped* 30–50-item AdvBench harmful-behaviour slice in English + a benign control; (2) translate EN→isiZulu by ≥2 routes (**NLLB-200 `zul_Latn`** + **Vulavula/Lelapa**, optional Google) so translation quality is a *measured variable*; (3) query isiZulu-capable models (**Aya-101 13B** primary; **InkubaLM-0.4B** runs-anywhere capability contrast); English = control arm; (4) score with Yong's **REJECT/BYPASS/UNCLEAR** on the back-translation, keyword classifier + LLM-judge, validated against a few human labels; (5) pair with a capability check (**Belebele `zul_Latn`** or **AfriMMLU `zul`**) so "refused because safe" separates from "can't read isiZulu." **Statistics (enforced, ties to 11.4):** refusal rate by language × route × model with 95% CIs (wide by design at n≈40); paired EN-vs-isiZulu on the same prompts. **Validity reflection (the payload):** name the confounds — translation-quality (a "refusal" may be the model failing to parse garbled MT; Yong's 53% vs 1% is *partly* because GPT-4 reads isiZulu well), capability/safety entanglement, who scores refusal and in what language, tiny-n + ethics (cap prompts; don't publish raw harmful outputs; responsible disclosure). The honest line: the interesting result is whether the gap **persists on open models**, **moves with translation quality**, **tracks isiZulu capability** — not "we reproduced 53%."
- Readings: Yong et al. `2310.02446` (operationalised); Inspect docs (optional framework); Masakhane/IrokoBench dataset cards.

## Verified reading list (headline claims full-text-checked 2026-06-25)

**Core:** Shevlane et al. `2305.15324` (dangerous-capability vs alignment/propensity split; "necessary but not sufficient"; **"the case for caution" is NOT in the paper — do not attribute**) · Phuong et al. `2403.13793` (four domains; no-safety-filters; "**no evidence of strong** dangerous capabilities… early warning signs"; elicitation/fine-tuning flagged as future work) · van der Weij et al. `2406.07358` (sandbagging = strategic underperformance; prompt + password-lock; target-accuracy calibration) · Meinke et al. `2412.04984` (in-context scheming; o1 across all six evals, >85% follow-up deception; gpt-4o none) · Raji/Bender et al. `2111.15366` (construct-validity anchor; the everything-benchmark critique) · Miller `2411.00640` (error bars; clustered SEs >3×; paired tests; power) · METR `2503.14499` (time horizon; logistic fit; hierarchical bootstrap).
**Reuse / supplementary:** Schaeffer et al. `2304.15004` (S2.4 metric mirage) · Casper et al. `2401.14446` (black-box access insufficient) · Needham/Apollo `2505.23836` (eval-awareness) · Manheim & Garrabrant `1803.04585` (Goodhart) · Yong et al. `2310.02446` (S1 anchor, lab).
**African-language substrate (verified isiZulu inclusion):** IrokoBench/AfriMMLU/AfriMGSM (`zul`), Belebele (`zul_Latn`), MAFAND-MT (`zul`), AfriQA (`zul`); models Aya-101 + InkubaLM; translation NLLB / Vulavula. (No off-the-shelf isiZulu *refusal* dataset exists — that gap is what makes the lab a contribution.)

## Source-verification log (2026-06-25)
Core papers checked against full PDF text (research agent). Two corrections carried into the build:
Phuong et al. is "**no evidence of strong** dangerous capabilities" (not "no strong evidence"); "the case
for caution" is **not** a Shevlane et al. phrase. African-language dataset isiZulu inclusion verified
per-dataset; uncertain resources (RTP-LX, MultiJail isiZulu coverage) excluded in favour of confirmed ones.

## Open choices for sign-off
1. **Lab model access:** Aya-101 (13B, real refusal signal, wants a GPU) via pre-loaded Colab/GPU (*recommended*) or API; keep InkubaLM as the runs-anywhere capability contrast. (If neither, the lab degrades to a capability-gap eval on InkubaLM.)
2. **Statistical depth (11.4):** *recommended* = "ceiling minus the bootstrap derivation" — binomial+Wilson CIs, clustered SEs, paired tests, power, and METR's logistic *presented* (not re-derived).
3. **S9/S11 red-teaming boundary:** confirm S11 = elicitation + eval-integrity (sandbagging/eval-awareness), S9 = red-teaming as attack methodology (already reflected in both curricula).
