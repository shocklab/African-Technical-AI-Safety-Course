# Harvard CS 2881R (AI Safety, Boaz Barak, Fall 2025) — pull for course revision

Source: https://boazbk.github.io/mltheoryseminar/ (fetched 2026-07-18, following Ben Sturgeon's
feedback doc + 2026-07-17 meeting). Companion resources: [YouTube lecture playlist](https://youtube.com/playlist?list=PL_b4B2IWlal3j01Rbj5ebT663E7x4bl_W),
[lecture notes on LessWrong](https://www.lesswrong.com/w/cs-2881r),
[intro blog post](https://windowsontheory.org/2025/07/20/ai-safety-course-intro-blog/).
Teaching fellows: Roy Rinberg (Ben's contact — happy to talk), Natalie Abreu, Hanlin Zhang, Sunny Qin.

Format worth noting: every lecture has 3–5 required pre-readings AND a student-run experiment
presented in class (the continuous research-practice component Ben flagged).

## Lecture schedule with pre-readings

| # | Topic | Pre-readings | Student experiment |
|---|-------|--------------|--------------------|
| Sep 4 | Introduction | "AI 2027"; Narayanan & Kapoor, "AI as normal technology"; METR measurement framework; Bostrom, Vulnerable World Hypothesis | Fine-tune on "good persona" outputs; test subtle alignment |
| Sep 11 | Modern LLM training | InstructGPT (Ouyang et al.); Constitutional AI (Bai et al.); DeepSeekMath (Shao et al.); DeepSeek-R1; Deliberative Alignment (Guan et al.) | Optimise prompt prefixes with policy-gradient methods |
| Sep 18 | Adversarial robustness, jailbreaks, injection, security | Carlini et al., adversarial alignment; Nasr et al., training-data extraction; Anderson, *Security Engineering* ch. 1–2; RAND, securing model weights | Red/blue team jailbreaks with test-time scaling |
| Sep 25 | Model specifications & compliance | OpenAI Model Spec; Zvi Mowshowitz commentary; SpecEval (Ahmed et al.); He et al., statutory interpretation for AI; Chatterji et al., ChatGPT usage | Compare system-prompt styles vs safety-training effects |
| Oct 2 | Content policies | Masnick on moderation; Newton on Facebook moderators; Wired on Google's image generator; OpenAI/Google/Midjourney policies | Evaluate open/closed models with jailbreak techniques |
| Oct 9 | Recursive self-improvement | Davidson, "Takeoff Speeds"; Davidson, Hadshar & MacAskill, intelligence-explosion types; Epoch AI GATE + AI 2030 | Does narrow task success require broad general skill? |
| Oct 16 | Capabilities vs safety | Becker et al., developer productivity; METR GPT-5 report; Anthropic RSP; OpenAI Preparedness v2 | TBD |
| Oct 23 | Scheming, reward hacking & deception | Greenblatt et al., alignment faking; Korbak et al., AI-control safety case; Schoen et al., anti-scheming training; Korbak et al., evaluating control measures | Impossible tasks trigger eval-hacking in coding agents |
| Oct 30 | Economic impacts | Jones, AI in R&D; Chatterji et al., ChatGPT usage economics; Brynjolfsson, Chandar & Chen, employment effects | TBD |
| Nov 6 | Interpretability | Baker et al., monitoring reasoning models; Chen et al., Persona Vectors; AxBench (Wu et al.); Sharkey et al., mech-interp open problems; Anthropic system card | TBD |
| Nov 13 | Emotional reliance & mental health | Habicht et al., therapy support; Moore et al., LLM limits in mental health; Song et al., chatbot experiences; Lopez, parasitic AI | TBD |
| Nov 20 | AI 2035 | TBD | Future research directions |

## Mapping onto our 24 sessions

**New sections agreed in the 2026-07-17 meeting:**
- **Model specifications** (Sep 25) → new sub-session beside 7.4 Whose constitution?. Activity as-is:
  read the OpenAI Model Spec, write your own. Pre-readings: Model Spec, Zvi commentary, SpecEval.
- **Recursive self-improvement & takeoff** (Oct 9) → new section, likely Session 2 or 3 territory.
  Pre-readings: Takeoff Speeds, intelligence-explosion types, Epoch GATE.
- **Model scheming** (Oct 23) → upgrade 3.4 (deception) and feed Session 10 (control). Pre-readings:
  alignment faking, control safety case, anti-scheming training.
- **Economic impacts** (Oct 30) → reading only, per meeting decision; deferred to the future
  Law/Science governance course. Candidate reading: Brynjolfsson, Chandar & Chen.

**Enrichment for existing sessions:**
- S1/S20: "AI as normal technology" (strong skeptic reading, fits S20 steelman), AI 2027,
  Vulnerable World Hypothesis. Plus Soares "Four Background Claims" + Tegmark Life 3.0 ch. 6
  (from Ben, not Harvard) for the superintelligence framing.
- S5–S7: DeepSeek-R1 and Deliberative Alignment are absent from our current post-training arc.
- S9: Carlini adversarial alignment; Nasr data extraction; RAND weights-security report;
  the security-engineering framing (Anderson ch. 1–2).
- S11–S12: METR GPT-5 report; Preparedness v2 (check against existing S12 RSP content).
- S13–S16: Persona Vectors (also connects to Ben's persona-across-languages point for the African
  framing), AxBench, Sharkey open problems.
- S20: emotional reliance / mental health readings as a present-harms extension.

**Format to consider:** the per-lecture student experiment (2–3 students present each session).
Roy Rinberg can advise on how it ran in practice.
