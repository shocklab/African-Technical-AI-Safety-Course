# Sessions 15–16 — Interpretability in practice (techniques, SAE lab, safety & limits)

**Week 8, Part IV.** Status: curriculum drafted 2026-06-25 from a survey (ARENA, the Transformer Circuits
thread, OpenAI/DeepMind SAE work, Neel Nanda) + literature **verified against the actual papers** (see
source log). Awaiting sign-off before building HTML.

## Where it sits, and the gap it fills

Session 13 gave the foundations; Session 15 gives the **techniques** that turn "this direction
correlates" into "this component causes" and "here is the feature basis": **activation patching**
(causal interventions) and **sparse autoencoders** (dictionary learning). Session 16 is the payoff and
the honesty: a hands-on SAE/steering lab, then what interpretability concretely **buys for safety**, its
**honest limits**, and the **sovereignty/African** close. The maths-honest additions: writing the SAE
objective down (sparse dictionary learning; L1 as a convex surrogate for L0; why TopK removes the
shrinkage bias) instead of treating SAEs as magic, and framing patching as causal-mediation analysis
with an explicit metric rather than a recipe. The course ethos shows hardest here: the 2024 SAE scaling
triumph is taught **alongside** the 2025 reassessment that SAE probes don't beat logistic regression on
downstream tasks.

**Coherence guardrails:** don't re-derive S13 (features/superposition/circuits — recap in one paragraph and hand off: S13 = "superposition exists", S15.3 = "so here's how we undo it") or S2.2 architecture. **Steering** is owned two ways: S10 used it as a *defence* (RepE / circuit breakers, Zou `2406.04313`); S15/S16 use it as a *technique* (difference-of-means vectors, feature clamping) — cross-reference, don't re-teach. The **15.4 ↔ 16.3 boundary**: 15.4 = limits *of SAEs as a technique* (do they work?); 16.3 = limits *of interpretability for safety* (does it yield guarantees?). Complementary, explicitly cross-referenced.

## Session 15 — structure (4 expository sub-sessions)

### 15.1 — Activation patching & causal interventions
Patching as causal-mediation analysis on the computation graph: the three runs (clean / corrupted / corrupted-with-restoration); resid-stream vs MLP vs attention patching; noising-vs-denoising; **attribution patching** (1 forward + 1 backward ≈ all patches, a Taylor approximation) and one line on causal scrubbing as the rigorous version. Be honest about what the intervention licenses (sufficient-to-restore on this distribution under this corruption — not "the component's purpose"). **Worked:** write the indirect-effect metric \(\mathrm{IE}=P_{*,\text{clean }h}[o]-P_*[o]\) and the attribution-patching first-order estimate \(\Delta L \approx (a_\text{clean}-a_\text{corrupt})\cdot\partial L/\partial a\); hand-trace one patch on a 2-layer toy.
- Readings: Meng et al. ROME `2202.05262` §2 (causal tracing); Nanda's activation/attribution-patching posts.

### 15.2 — The IOI circuit: a worked end-to-end reverse-engineering
"When Mary and John went to the store, John gave a drink to ___" → "Mary". The **26-head, 7-class** circuit (Name Mover, S-Inhibition, Duplicate Token, Induction, Previous Token, Backup & Negative Name Movers) mapped to the human algorithm; **path patching**; metric = **logit difference**. The honest punchline: the circuit is **87% faithful** but **fails the hardest completeness/minimality tests**, and **Backup Name Mover heads silently take over when Name Movers are ablated** — real circuits are messy, faithfulness ≠ completeness. **Worked:** logit difference = logit(IO) − logit(S); why patching from the ABC distribution drops it.
- Readings: Wang et al. *Interpretability in the Wild* `2211.00593` §3–4.

### 15.3 — Superposition → dictionaries → sparse autoencoders & monosemanticity
From superposition (2-sentence recap) to "recovering features = sparse dictionary learning." The canonical SAE; expansion factor / overcomplete dictionary; training on residual-stream activations; autointerp evaluation; the scaling arc (Bricken toy → Templeton's Claude 3 Sonnet, 34M features / ~12M alive, the **Golden Gate Bridge** feature that fires across languages and images and steers the model when clamped); the dead-latent problem. **Worked (centrepiece):** put the SAE loss on the board — \(L(x)=\lVert x-\hat x\rVert_2^2 + \alpha\lVert c\rVert_1\), \(c=\mathrm{ReLU}(Mx+b)\), \(\hat x=M^\top c\) — explain L1 as a convex surrogate for L0 and its activation-shrinkage bias; then **TopK** (\(z=\mathrm{TopK}(W_\text{enc}(x-b_\text{pre}))\), loss \(=\lVert x-\hat x\rVert_2^2\), no L1) and why it removes the bias; sketch the \(L(N,k)\) scaling-law shape.
- Readings: Cunningham et al. `2309.08600` §2 (the ReLU+L1 SAE); Bricken et al. *Towards Monosemanticity* (transformer-circuits.pub 2023); Gao et al. *Scaling & evaluating SAEs* `2406.04093` §2 (TopK, scaling laws); Templeton et al. *Scaling Monosemanticity* (2024) — Golden Gate.

### 15.4 — The honest current state of SAEs
The reconstruction-frontier-isn't-the-goal point (Gao §4) → downstream metrics. The **2025 reassessment**: Kantamneni/Engels et al. (113 probing datasets, four hard regimes) find **SAE probes do not beat logistic-regression probes on raw activations** under a fair "quiver of arrows" protocol, and the earlier positive results leaned on **weak baselines** (max-pooling a non-privileged basis); SAE latents also **fail OOD** (the "living room" latent fires in English, near-dead in French — relevant to the African question). DeepMind's negative downstream results and **deprioritisation** of fundamental SAE research; "SAEs discard task-relevant information." The careful, non-nihilistic conclusion: still useful for exploration/dataset-debugging; the norm is rigorous baselines. (Forward-ref 16.3 for the broader safety-guarantee critique.)
- Readings: Kantamneni/Engels et al. `2502.16681` §1,3,5,7; DeepMind 2025 SAE-deprioritisation post.

## Session 16 — Lab + safety applications & limits (4 pages: 1 lab + 3 content)

### 16.1 — Lab: steering + interpreting SAE features
**Track A (CPU floor) — activation steering:** build a steering vector as the **difference of mean residual-stream activations** between two prompt sets, inject \(\alpha v\) at a layer, sweep \(\alpha\)/layer, watch behaviour shift and break (opens with "you saw directions used defensively in S10; here you build one"). **Track B (CPU-feasible / GPU-optional) — SAE features:** load a pretrained gpt2-small SAE via SAELens, find firing features, **interpret 3–5 by hand** (top-activating contexts + monosemanticity verdict), **ablate one** and observe the logit effect; GPU stretch: *train* a small SAE on Pythia-70M residual stream (~1 GPU-hr on the `l40s` partition), plot the reconstruction-vs-sparsity Pareto curve. **Honesty hook:** train a logistic-regression probe on raw activations vs an SAE-feature probe for one concept — feel the 15.4 result.

### 16.2 — What interpretability buys for safety
The white-box arm of the S8.1 oversight / S11 evals stack, as a rising-then-falling arc: **CCS** (Burns — an unsupervised probe finds latent "knows ≠ says", holds when the model is prompted to answer falsely) → **its refutation** (Farquhar et al. — arbitrary binary features satisfy the CCS loss; it tracks the most *salient* feature, not truth) → **RepE** (Zou — read & control concepts; +18 pts TruthfulQA; the read-vs-control-vs-understand distinction; link S10) → **Sleeper Agents** (Hubinger — backdoors survive RLHF/SFT/adversarial training; the motivating hard problem; interp defences surveyed, not solved) → **the auditing game** (Marks et al. — blind red/blue; the SAE team cracked a hidden objective in 90 min, the **API-only team failed**; honestly caveated as "unrealistically easy"). The arc *is* the pedagogy.
- Readings: Burns et al. `2212.03827`; Zou RepE `2310.01405` §4; Marks et al. *Auditing Language Models for Hidden Objectives* `2503.10965`; background Hubinger et al. *Sleeper Agents* `2401.05566`.

### 16.3 — The honest limits of interpretability
Equal weight to 16.2. **Illusions:** Bolukbasi et al. (a "song-titles" neuron means different things on different datasets — always test on multiple datasets); Makelov/Nanda (a subspace patch can "succeed for the wrong reason" via a dormant pathway). **Scalability:** Lieberum/Nanda Chinchilla — the *mechanics* scale to 70B but *semantic understanding* is mixed. **State of field:** Sharkey/Nanda et al. *Open Problems* — SAEs lack solid theory, features are dataset-dependent, superposition may be only pragmatically valid, downstream usefulness under-tested; **formal verification is well beyond current capability**. The **"streetlight" critique** taught as a named lens grounded in those results. The synthesising thesis (quotable): realising interp's benefits "will require careful attention to the risks of... giving **false assurance** about AI safety."
- Readings: Sharkey/Nanda et al. *Open Problems in Mech Interp* `2501.16496` (intro + conclusion); Farquhar et al. `2312.10029`; background Bolukbasi `2104.07143`, Makelov `2311.17030`, Lieberum `2307.09458`, Nanda "Longlist of Theories of Impact".

### 16.4 — Interpretability, sovereignty, and the (thin) African angle
The strongest *honest* angle, led by a verified datapoint: in the auditing game the **API-only team failed while weight-access teams succeeded** — *access tier determines whether you can audit at all* (ties S10 "who holds the keys", S12 audit/access). Then English-centrism: interp findings are English-validated, the isiZulu safety gap (S1/S9) would likely be **invisible** to off-the-shelf interp (you can't read a concept you haven't elicited), with the circuit-breakers multilingual table as a concrete, capability-confounded datapoint. Then the **compute cost** of interpreting (who can afford a 1M-wide SAE on a frontier model). An explicit **honesty box**: "this is the course's thinnest African angle — there is no isiZulu SAE, no African interpretability dataset; we are flagging research gaps, not reporting results — and that gap is a legitimate thing for you to work on." Ends with an optional **project brief** (does a 'refusal'/'harmfulness' direction exist in an isiZulu-prompted open model, and can you read it?).

## Verified reading list (full-text-checked 2026-06-25)
**Techniques:** ROME `2202.05262` (causal tracing; early-site middle-layer MLPs at last subject token; rank-one edit) · IOI `2211.00593` (26 heads/7 classes; 87% faithful; backup heads; fails completeness) · Cunningham `2309.08600` (SAE loss \(\lVert x-\hat x\rVert_2^2+\alpha\lVert c\rVert_1\); more interpretable than PCA/neurons; recon-loss caveat) · Bricken *Towards Monosemanticity* (1-layer, 512-neuron MLP, 512–~131k features, MSE+L1, feature splitting — feature *examples* flagged illustrative) · Templeton *Scaling Monosemanticity* 2024 (Claude 3 Sonnet; 34M features/~12M alive; Golden Gate multilingual+multimodal, clamping steers) · Gao `2406.04093` (TopK SAE, no L1; 16M latents on GPT-4; scaling laws; dead latents 7% at 16M) · Kantamneni/Engels `2502.16681` (SAE probes ≯ logistic regression across 113 datasets; weak-baseline illusion; OOD failure).
**Safety apps:** Burns CCS `2212.03827`; Farquhar `2312.10029` (CCS refutation); Zou RepE `2310.01405` (+18 TruthfulQA); Hubinger Sleeper Agents `2401.05566`; Marks auditing game `2503.10965` (API team failed; SAE 90-min crack; "unrealistically easy" caveat).
**Limits:** Bolukbasi `2104.07143`; Makelov `2311.17030`; Lieberum Chinchilla `2307.09458`; Sharkey/Nanda Open Problems `2501.16496`; Nanda theories-of-impact (Alignment Forum).

## Source-verification log (2026-06-25)
Two research agents checked all primary papers against full text. Confirmed: ROME causal-tracing metric + localisation; IOI head count/faithfulness/backup-heads; the SAE objectives (ReLU+L1 and TopK), Templeton scale figures, Gao scaling/dead-latents; the 2025 SAE reassessment numbers; CCS + Farquhar refutation; RepE TruthfulQA gain; Sleeper Agents (interp defences surveyed not solved); the auditing-game access-tier result. **Flag:** Bricken's specific feature *examples* (Arabic/DNA/base64) couldn't be re-read directly (transformer-circuits HTML exceeds fetch size) — cite as "illustrative, per Bricken et al." or open in a browser before publishing.

## Open choices for sign-off
1. **S16.1 lab emphasis:** SAE-interpretation as the main course + steering as a required short warm-up — *recommended* (ties tightest to 15.3/15.4) — vs steering-primary.
2. **How hard to lean on the 2025 SAE negative results (15.4):** keep the full 15.4 sub-session — *recommended*, it's about the technique's validity and cutting it would be dishonestly triumphalist — coordinated so 16.3 carries the broader safety-guarantee critique.
3. **GPU in the lab:** SAE-training as a clearly-optional GPU stretch on the cluster — *recommended* — vs pretrained-SAEs-only (most equitable) vs required (assumes cluster access for all).
4. **16.4 ends with an optional project brief** (the isiZulu-feature question) — *recommended*, converts the thin angle into a generative one.
