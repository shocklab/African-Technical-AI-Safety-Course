# Session 10 — Unlearning & the AI-control agenda

**Week 5, Session 2** (Session 9 is the first). Status: curriculum drafted 2026-06-25 from a survey of
existing courses + literature **verified against the actual papers** (see source log). Awaiting sign-off.

## Where it sits, and the gap it fills

Two damage-bounding paradigms that usually live apart: **unlearning** (remove a capability/knowledge
after training) and **AI control** (assume the model may be scheming and design protocols that stay
safe anyway). The honest, maths-first version foregrounds three things the popular treatments bury:
(1) control's "safety" is a *probability against a specific attack policy*, not a guarantee; (2) current
unlearning mostly **obfuscates rather than erases** (now the central result of the area); (3) both lean
on a weaker *trusted* component (a trusted monitor, a retain set, a held-out probe) — exactly where
compute scarcity and language coverage bite. Control is a Redwood research programme (not yet textbook);
BlueDot now teaches a "robustness, unlearning and control" unit, so contrasting control with S8.1
oversight is standard, not novel.

**Coherence guardrails (reference, do not re-derive):**
- S3 (deception/scheming/power-seeking): control *consumes* this threat model — "assume the model may be scheming (S3)" and move on.
- S6/S7 (RLHF/RLAIF): unlearning and circuit-breaking are *post-hoc edits* downstream of alignment training; don't re-explain RLHF.
- S8.1 (oversight): draw the contrast (oversight *aligns*; control *contains under assumed misalignment*) but don't re-teach debate/amplification/W2S/sandwiching.
- S9 (robustness): GCG / low-resource jailbreaks are the *adversary class* against which safety numbers are quoted; point back for attack mechanics.
- S11 (evals): WMDP-as-a-dangerous-capability-eval and "evals must be multilingual" are S11's; here use WMDP only as an *unlearning* target/metric.
- S12 (governance): tiered API access, open-weight release policy, compute thresholds are S12; note unlearning + structured access are complements, then defer.

## Session-level learning objectives

By the end a student can: (1) distinguish exact vs approximate unlearning and state the indistinguishability ideal, and why it is hard to *verify*; (2) explain why naïve gradient ascent fails and read the Who's-Harry-Potter and RMU constructions; (3) state the control thesis, define trusted vs untrusted models, and read a control evaluation as a red/blue game whose safety is a probability; (4) locate control protocols on the safety/usefulness Pareto frontier and explain untrusted-monitor collusion + countermeasures; (5) give the honest bottom line — unlearning obfuscates more than it erases; control buys a bounded, attacker-relative probability — and write a threat-model accounting for any safety claim.

## Proposed structure — 5 sub-sessions (4 expository + 1 lab)

### 10.1 — Machine unlearning: what it is, and why "forget" is hard to define
Exact (retrain on \(D\setminus\text{forget}\)) vs approximate; the indistinguishability ideal; the three regimes (privacy/RTBF, copyright, safety) and why they differ (privacy tractable, capability control not). Who's-Harry-Potter as intuition pump; TOFU as the *measurement* breakthrough; knowledge ≠ capability (recombination). **Worked:** (a) why naïve gradient ascent is pathological (the cross-entropy gradient shrinks as p→1, promoting the *second* token) vs Eldan–Russinovich's \(v_{\text{generic}}=v_{\text{base}}-\alpha\,\mathrm{ReLU}(v_{\text{reinf}}-v_{\text{base}})\); (b) walk TOFU's **KS-test** forget-quality metric on toy CDFs (high p = good forgetting — a satisfying inversion of significance logic). **African hook:** data sovereignty — can a community's withdrawn-consent corpus actually be removed? TOFU's "rare in pretraining" precondition holds *better* for low-resource data.
- Readings: Eldan & Russinovich `2310.02238` §2; TOFU `2401.06121` §2.2; Open Problems `2501.04952` §1–2.

### 10.2 — The control paradigm: assume scheming, bound the damage anyway
The control thesis; trusted vs untrusted models operationally; a control evaluation as red/blue game; safety = probability against an attack policy. Position vs S3 (consumes the threat model) and S8.1 (aligns vs contains). The APPS backdooring testbed; the two baselines (don't-use-U: 100% safe / 2% useful; upfront auditing: 100% useful / **15%** safe). **Worked:** derive upfront-auditing safety analytically and show it is **scale-invariant** (double the problems + budget, attacker halves the per-problem backdoor rate, win probability fixed) — motivates why monitoring beats auditing. **African hook:** *who holds the keys?* The protocol presupposes ownership of the trusted model T and scarce trusted labour H; a downstream operator consuming a frontier API owns neither and cannot run it — control is an affordance of the stack owner.
- Readings: Greenblatt et al. `2312.06942` §1–2; AISES §3.2 (Monitoring).

### 10.3 — Control protocols and the safety/usefulness frontier
Read the safety–usefulness plane as a Pareto frontier. Trusted monitoring (62%/97%); defer-to-trusted sweep (10%→83%/93%, 20%→92%/83%, 50%→100%/51%); untrusted monitoring (naive → **0%** under "pretend not to see backdoors" collusion; recovered to 79%/96% via synthetic-backdoor eval + **redaction**); trusted editing (92%/94%, Pareto-dominates). **Worked:** collusion-as-Bayesian-updating made quantitative — the synthetic-to-real ratio sets the monitor's prior; scaling synthetic evals makes any fixed collusion signal eventually fail (collusion gets *harder* at scale); students compute the likelihood ratio + break-even episode count. **African hook:** the trusted monitor is the weak link, and it is weakest in low-resource languages (Circuit Breakers' multilingual Table 6: residual ASR varies by language tier) — the same protocol delivers *less* safety for African-language deployments.
- Readings: Greenblatt et al. `2312.06942` §3 + §3.4.2 (collusion); Circuit Breakers `2406.04313` §3–4.

### 10.4 — Limits, and where unlearning + control actually fit
The honest bottom line. Łucki et al.: RMU's WMDP-Bio recovered from 29.9% to **62.4%** (fine-tune on 5 forget samples), **61.6%** (10 *unrelated* samples), **64.7%** (orthogonalisation), <2pp MMLU cost — knowledge suppressed, not removed; black-box evals lied. TAR resists hundreds of fine-tuning steps (vs RMU broken in <20) but at **−10.6pp MMLU**, PEFT-fragile, with a data-contamination correction in its own history (a reproducibility teachable moment). Open Problems' synthesis: dual-use re-emerges by recombination; verification unsolved. Control's own scope limits (black-box only; U not trained; one testbed; safety = min-max over *imagined* attacks). **Worked:** a threat-model accounting — for each claim ("robust to GCG 2,500 steps"; "broken by 10-sample fine-tune") write the exact quantifier (input- vs weight-space adversary; black- vs white-box). Lesson: a safety number is meaningless without its adversary class. **African hook (developed — see below):** open-weight tamper-resistance is the only lever a downstream operator has, yet the most fragile/compute-hungry one.
- Readings: Łucki et al. `2409.18025` §4–6; TAR `2408.00761` §5 + limitations; Open Problems `2501.04952` §4.

### 10.5 — Lab: does "unlearning" actually remove knowledge? (CPU-floor + optional GPU)
**Pure-CPU graded core (recommended):** build a **trusted monitor**. Given clean and weakly-backdoored Python snippets (APPS `is_odd`-style special-case backdoor), build a cheap suspicion scorer (logistic-regression / small model), set a 2% false-positive threshold, measure catch-rate; then add a trivial **collusion signal** (while-loop-for-loop swap) and a **redaction** countermeasure and watch the safety number move — instantiates 10.2–10.3 with no large model. **Optional GPU extensions:** (a) logit-lens elicitation of "forgotten" WMDP knowledge from the `cais/Zephyr_RMU` checkpoint (forward passes only); (b) LoRA-relearn on 10 unrelated examples → WMDP-Bio jumps back (the Łucki headline). **Deliverable:** notebook + one paragraph: "Was the knowledge removed, or hidden? What evidence distinguishes them?"

## Verified reading list (all full-text-checked 2026-06-25)

**Core:** Greenblatt, Shlegeris et al. `2312.06942` (AI Control; trusted GPT-3.5 / untrusted GPT-4; safety = P(no backdoor over 5,000 problems); frontier numbers above; training of U *not* evaluated) · Li et al. WMDP+RMU `2403.03218` (3,668 MCQ; Zephyr Bio 63.7→31.2, Cyber 44.0→28.2, MMLU 58.1→57.1; robust to GCG/probes; **finetuning outside threat model**) · Eldan & Russinovich `2310.02238` (Who's Harry Potter; ~1 GPU-hr; the generic-label construction; admits leaks) · Maini et al. TOFU `2401.06121` (200 fictitious authors; forget quality = KS-test p-value; no baseline crosses p=0.05 without wrecking utility) · Łucki et al. `2409.18025` (the adversarial twist; recovery numbers above) · Zou et al. Circuit Breakers `2406.04313` (representation rerouting; ASR ↓~87–90%, <1% capability hit; multilingual Table 6 = African-lens data).
**Supplementary:** Tamirisa et al. TAR `2408.00761` (tamper-resistance; −10.6pp MMLU; contamination correction) · Barez et al. Open Problems `2501.04952` (capability-control ≪ privacy; recombination; verification open).

## Source-verification log (2026-06-25)
Six core + two support checked against full PDF text (research agent). All numbers above confirmed, including the control frontier (Table 7), WMDP/RMU deltas, TOFU's KS-test framing, and Łucki's recovery figures. The "unlearning obfuscates, not erases" framing is *supported by the verified evidence*, not editorial spin.

## Open choices for sign-off
1. **Lab core track:** pure-CPU trusted-monitor + collusion build (*recommended* — runs for every student, exercises the most distinctive idea) with logit-lens / LoRA-relearn as optional GPU extensions.
2. **Paper density:** 6 core + 2 support is heavier than S6/S7 (~6 total). Option to demote TAR and Who's-Harry-Potter to "further reading" (keep one key result each in-text), leaving 4 core + Circuit Breakers.
3. **Framing stance:** land S10 on "these are damage-bounding tools with quantifiable limits, not solutions" (*recommended*, matches the course's honest-pushback ethos; verified-evidence-backed) — confirm this deliberate stance.
