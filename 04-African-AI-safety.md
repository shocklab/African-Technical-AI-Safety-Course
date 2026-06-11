# African AI safety — integration map

A cross-cutting thread, not a single week. The goal is to fold African AI safety in where it is
*genuinely strong and genuinely technical*, and to make **"whose safety, whose risks, whose values,
who sets the agenda?"** a live through-line — without tokenism.

> **Honest framing (say this to the class).** The core technical-alignment agenda — interpretability,
> scalable oversight, control — is overwhelmingly Northern; there is little African literature in it.
> That gap is itself a teachable fact (who has the compute, who funds the agenda, whose risks get
> counted). African contributions are real and strong in **low-resource-language safety, evaluation,
> governance, data sovereignty, and the relational-ethics / present-harms critique** — which is exactly
> where this course leans on them.

---

## The flagship hook: African languages are a frontier safety hole

**Yong, Menghini & Bach, "Low-Resource Languages Jailbreak GPT-4"** (arXiv **2310.02446**; SoLaR @
NeurIPS 2023 **Best Paper**): translating unsafe prompts into low-resource languages — **isiZulu**
included — bypassed GPT-4's guardrails on ~79% of AdvBench behaviours, vs ~1% in English. Safety
training and evals are English-centric, so frontier models are *measurably less safe in the languages
our students speak.*

This single result turns "African AI safety" into a **robustness + evaluation problem at the technical
core of the course**, not a garnish. It anchors a lab (S9), an eval (S11), and a flagship project.

---

## Session-by-session thread

| Session | African-safety content | Sources |
|---|---|---|
| **S1 — Framing** | Whose risks count? Introduce the present-harms-vs-x-risk debate *with its North/South dimension* as part of the opening, not an afterthought. | Hanna & Bender, *SciAm* 2023; Birhane, *Patterns* 2021 |
| **S4 — Physical substrate** | Compute **and data** sovereignty as the African angle on "compute is the floor"; the pledge-vs-reality gap. | AU Data Policy Framework (2022); the $60bn-pledge case study |
| **S8 — Whose values?** | Ubuntu / relational ethics as a tool for value specification & preference aggregation (already via Gen AI Week 4); add Birhane's relational ethics explicitly. | Mhlambi, "From Rationality to Relationality"; Birhane, *Patterns* 2021 |
| **S9 — Robustness** ⭐ | **Multilingual jailbreaks** as a core example + lab: translate an AdvBench-style refusal set into isiZulu/isiXhosa, measure refusal-rate degradation vs English (API/small-model, Colab-fine). | Yong et al. 2310.02446 |
| **S11 — Evals** ⭐ | Build an **African-language safety eval in Inspect** on open Masakhane data; discuss LLM-judge bias for African contexts (emerging research — present as open). | IrokoBench 2406.03368; AfriQA 2305.06897; Global-MMLU 2412.03304 |
| **S12 — Governance** | African-grounded governance: the **RIA Just AI framework**, AORAI, the **AU Continental AI Strategy (2024)**, and the data-protection stack students actually operate under (**POPIA**, Malabo Convention). | Reuel et al. (taxonomy) + the African instruments below |
| **S18 — Dedicated session** ⭐ | "AI safety from the Global South" — see outline below. | (whole section) |
| **S20 — Skeptics** | The Global South present-harms critique is a *central* skeptic position, not a fringe one; run it as a real debate with the PNAS rebuttal. | Hanna & Bender; Birhane; *PNAS* 2025 counterpoint |
| **Projects (S17, S23)** | A flagship archetype: replicate Yong et al. on locally relevant SA languages with **InkubaLM**/Aya + an IrokoBench split. | below |
| **S24 — Pathways** | African pathways: Deep Learning Indaba, ILINA, AI Safety East Africa, Masakhane, Lelapa. | below |

---

## Session 18 outline — "AI safety from the Global South"

**Objectives.** Articulate the present-harms-vs-existential-risk debate and its North/South dimension;
explain decolonial-AI and compute/data-sovereignty arguments; name real African-led safety/eval work
and assess the gap.

**Pre-class.**
- Hanna & Bender, "AI Causes Real Harm. Let's Focus on That over the End-of-Humanity Hype" (*Scientific
  American*, 2023) — the most assignable short statement of the present-harms view.
- Mohamed, Png & Isaac, "Decolonial AI" (2020).
- **Counterpoint for balance:** "Existential risk narratives about AI do not distract from its immediate
  harms" (*PNAS* 2025) — so the debate isn't one-sided.
- Skim: ILINA Program site; AU Continental AI Strategy executive summary.

**In-class.** (i) Structured debate: half steelman "focus on present harms," half steelman "long-term
risk matters too," then swap — close on which disagreements are empirical vs values-based. (ii) Mini-
lecture on compute/data sovereignty and the **$60bn Kigali pledge vs infrastructure reality** (still
routes through Nvidia GPUs + Big-Tech data centres) as a live case study. (iii) ILINA as proof African-
led technical x-risk/eval work exists. **Natural guest-lecture slot** (see candidates).

---

## People & guest-lecturer candidates (verified affiliations, June 2026)

- **Rachel Adams** — CEO, Global Center on AI Governance (runs AORAI); **honorary research fellow, UCT
  Ethics Lab** → strongest *local* guest. https://www.globalcenter.ai/about/rachel-adams
- **Vukosi Marivate** — Assoc. Prof., Univ. of Pretoria; co-founder Masakhane, Lelapa, Deep Learning
  Indaba → the African-NLP + ecosystem voice.
- **Pelonomi Moiloa** (CEO) / **Jade Abbott** (CTO) — Lelapa AI → applied, model-building, InkubaLM.
- **Cecil Abungu** — ILINA Program (Cambridge / Strathmore-linked) → African-led AI-safety/GCR voice.
- **Sabelo Mhlambi** — Berkman Klein / Carr Center → Ubuntu & AI governance.
- **Abeba Birhane** — Trinity College Dublin, AI Accountability Lab → relational ethics, dataset audits,
  present-harms critique. (Diaspora; likely remote.)
- Also: **Chinasa T. Okolo** (Brookings — Global South AI governance/evaluation), **Melissa Omino**
  (CIPIT Strathmore — African data governance), **David Adelani** (MasakhaNER/IrokoBench lead — African-
  language evaluation), **Marie-Therese Png** (Oxford — decolonial AI), **Timnit Gebru** (DAIR).

## Orgs & open resources usable on Colab

- **Masakhane** (https://www.masakhane.io/) — 400+ open African-NLP models, 20+ datasets; the data
  backbone for safety-eval projects.
- **Lelapa AI — InkubaLM-0.4B** (https://huggingface.co/lelapa/InkubaLM-0.4B) — 400M-param open SLM
  (isiZulu, Yoruba, Hausa, Swahili, isiXhosa); small enough to run/probe on Colab.
- **Cohere For AI — Aya** (https://cohere.com/research/aya) — open multilingual models + the "language
  gap" framing.
- **Benchmarks (open):** IrokoBench → AfriMMLU/AfriMGSM/**AfriXNLI** (arXiv 2406.03368, in lm-eval-
  harness); AfriQA (2305.06897, CC-BY-NC-4.0); MasakhaNER 2.0; MasakhaNEWS.
- **African AI-safety community:** **ILINA Program** (https://www.ilinaprogram.org/); **AI Safety East
  Africa** (runs the BlueDot AISF curriculum, https://aisea.magentaai.org/). ⚠️ **Equiano Institute**
  bills itself as an Africa AI-safety lab but looks early-stage — verify activity before relying on it.

## Policy & data sovereignty (verified)

- **AU Continental AI Strategy** (2024; Accra, July 2024) — five focus areas: harness benefits, build
  capabilities, **minimise risks**, stimulate investment, foster cooperation; implementation 2025–2030.
- **Africa Declaration on AI** — Global AI Summit on Africa, Kigali, April 2025.
- **$60bn "Africa AI Fund"** — ⚠️ a 2025 Kigali *pledge*, **largely unrealised / on paper**, and tied to
  the Kigali declaration **not** the 2024 AU Strategy. Teach as an ambition-vs-infrastructure case study,
  not a funded programme.
- **Data sovereignty:** CARE Principles (Indigenous-data — adapt, don't apply wholesale); AU Data Policy
  Framework (2022); Malabo Convention (in force 2023); **POPIA** (South Africa, 2021) — ground a "where
  did your eval data come from, and may you use it?" exercise in the law students actually operate under.

---

## Flagship student project

**"Does the guardrail hold in isiZulu?"** Take InkubaLM or Aya (+ an IrokoBench/AfriQA split),
translate a small AdvBench-style refusal set into isiZulu/isiXhosa (or another SA language), and measure
refusal-rate degradation vs English — a self-contained, Colab-feasible replication/extension of Yong et
al. on locally relevant languages. Variants: extend to an Inspect eval; test whether a system-prompt or
few-shot mitigation closes the gap; audit an open African-language dataset for safety-relevant content.

---

## Integrity caveats (don't overclaim)

1. There is little African work in *core* technical alignment — name the gap and its causes rather than
   papering over it.
2. The $60bn fund is a pledge, largely on paper, and separate from the AU Strategy.
3. LLM-judge bias "for African contexts" is preprint-level — present as open research.
4. Equiano Institute / AfriClimate AI / AfriStereo: real but early-stage or unverified for licence/safety
   profile — confirm before relying on them.
5. The "real harms over hype" *Scientific American* essay is **Hanna & Bender**, not Birhane; Birhane's
   citable anchor is the *Patterns* relational-ethics paper.
6. Run the whole reading list through `/verify-references` before publishing — exact IDs/stats included.
