# Eval Atlas fact-check, 3 Nov 2026

Read-only review of `data/benchmarks.json` (90 entries) and `data/gaps.json` against the papers. Tags: **ERROR** = factual (the paper says otherwise); **JUDGEMENT** = rubric call where we'd score differently; **INCLUSION** = possible breach of the inclusion rule.

## Summary

**Counts**
- Entries checked: 90. All 90 against full text: 88 via arXiv HTML/PDF, plus isaaclab-eval and radeis via their GitHub READMEs. None against the abstract alone.
- Entries with at least one factual error: 49. About half are metadata only: missing or outdated venue/authors, missing `code` link, `avail` wrong.
- Entries with judgement-call disagreements: 22. Of these, 11 have no factual error.
- Inclusion flags: 6 (hasard, labsafety, labvla, l3-bench, simuguard, trust-cot).
- Links: every `url` and `code` returns 200 except two `code` links, which 404: annie and no-instruction.

**Highest-impact corrections**
1. **rctf2**: fidelity `real` → `closed_sim`. RCTF2 runs in Docker containers, not on real robots. avail `open` → `restricted`: the Jeopardy CTFs ship only in CAI PRO. Summary: drop "on real robot platforms". This is the atlas's only dangerous-capability evaluation with robots as target, and g2 and g8 cite it.
2. **abc-bench**: xr 3 → 2 (JUDGEMENT, medium). The only task executed physically is a benign Gibson assembly; the dual-use steps stay digital. This is the atlas's only xr-3 entry, so g2's headline claim depends on it.
3. **responsible**: fidelity drop `real`. The paper is CoppeliaSim-only and lists real hardware as future work.
4. **tapdreamer**: fidelity add `real`. It was also validated on a real SO-101.
5. **l3-bench**: fidelity `open_loop` → none. The paper runs no evaluation at all, and its cx/dex/cog scores rate a hypothetical protocol. Also an INCLUSION flag.
6. **Fidelity wrong in six more entries**:
   - patch-rokae: add `closed_sim` (main results are on LIBERO).
   - health-attendant: `closed_sim` → `open_loop` (mock acknowledgement server).
   - infectbot and comms-attacks: `open_loop` → `closed_sim` (both run in Isaac Sim).
   - shawshank: `closed_sim` → `open_loop`.
   - radeis: `closed_sim` → `qa`.
7. **avail wrong**:
   - `paper` → `open`: homesafe-bench, safemanip, upa-rfas, labvla, robotrust, health-attendant, labference, dexbiolab, robogate (HF data). safestage: `announced` → `open`.
   - `open` → `announced`/`paper`: annie (repo empty, code URL 404), no-instruction (repo 404), pipette (repo 404), safevla ("will be released"), robobugbench (no URL given).
   - Also unconfirmed: tsha, agentsafe, attackvla (no code link in the paper).
8. **Wrong tags**:
   - robopair: `drone` domain, but no drone is tested.
   - embodiedlab: `bio_uplift`, but it covers physics and chemistry, with no biology.
   - behavior1k: arch `vla, vlm_agent`, but only RL baselines are evaluated.
9. **Wrong numbers or summary**:
   - safevla: atlas has v1 figures. v3 reports 27 entries and 38–56%.
   - robogate: 50,000+ runs → 40,000+.
   - pipette: "ACT 60.3%" is not in the paper.
   - siren: 3× is 1.86× in the paper body; the paper is internally inconsistent.
   - vla-arena: five suites are safety suites, not one.
   - labvla: the summary describes a model paper as an evaluation.
10. **Venues to update** (about 15): LabSafety (Nat Mach Intell 2026), ABC-Bench (ICML 2026), UPA-RFAS (CVPR 2026), ICAT (NeurIPS 2026), InfectBot (IJCAI 2026), patch-rokae (RA-L 2026), drone-physical (CACM 2026), health-attendant (R. Soc. Open Sci. 2026), blindfold (SenSys 2026), RoboTrust (EMNLP Findings 2026), HASARD (ICLR 2025), IndustryEQA (NeurIPS 2025 D&B), and others below.

**Gap-finding claims that would break**
- **g2** "ABC-Bench is the only surveyed work that measures a catastrophic capability through to physical execution". This breaks if abc-bench goes to xr 2: no entry would score xr 3, and "ten further works" becomes eleven. Even at xr 3, "assemble DNA" should say a benign construct.
- **g6** "in simulation (TAPDreamer) and on a physical robot (PASA-KV)". TAPDreamer also ran on a real SO-101. Also, "Humanoids appear in ReactHuman, WorldFailBench and SIREN" is incomplete: humanoid-orch (Unitree G1 orchestrator), isaaclab-eval (GR1 humanoid tasks) and egosafety (humanoid viewpoint) are also tagged or described as humanoid. "No safety benchmark evaluates a learned policy on a real humanoid" still holds.
- **g8** "24 surveyed works that involve real hardware". With the high-confidence fidelity fixes the count is **23**: minus responsible and rctf2, plus tapdreamer. It is 24 if behavior1k's Tiago sim-to-real study is counted (low confidence). "CAIBench RCTF2 (22% solved)" should read "best agent solves 22% (6 of 27)". The sentence survives because it does not claim real robots, but it must not be read as hardware. "RoboHarm, which uses Inspect Robots as its harness" is verified.
- **g3** "18 surveyed works that are demanding in both respects" (dex ≥ 2 and cog ≥ 2). The count becomes **15** if the dex 2 → 1 calls on responsible, inspect-robots and reacthuman are accepted (all three act through primitives or a pre-trained controller), and 14 if l3-bench (no experiments) is dropped. "Six are capability suites" still holds. "No safety benchmark combines demanding manipulation with causal/strategic reasoning" still holds: the only dex ≥ 2 and cog 3 entry is embodiedlab, a capability suite.
- **g4** "CAPSafe … report[s] a corresponding gap between recognition and action". CAPSafe's gap is recognition vs plan, in a text simulator. "Beyond Behaviour … describes its methods only briefly" is weak: it is a 4-page paper with a detailed methods appendix. Say "a short paper" instead. All RoboHarm and Refuses When Asked figures are verified.
- **g7** "L3-Bench … its abstract reports no experimental results". The whole paper reports none, so strengthen the wording. LabSafety Bench (no robotics link) and LabVLA (a model paper whose only reusable measure is LabUtopia) carry INCLUSION flags. If they are removed, g7's lists shrink but the argument holds. EmbodiedLab is physics and chemistry, not biology; g7 does not claim bio, so it is unaffected.
- **Unaffected**:
  - g1: three loss-of-control works. The external RepliBench, Agent Matrix and AgentMisalignment links resolve to the named papers.
  - g5: EAPrivacy's "up to 86%" is verified; the three misalignment-tagged works match.
  - g9: power and disempowerment each have exactly one entry, as stated.
  - If drone-physical's `infrastructure` → `violence` call (low) is taken, the infrastructure row loses one entry; no prose depends on it.

---

# Findings by entry
## responsible (ResponsibleRobotBench)
- ERROR · fidelity · `closed_sim, real` → `closed_sim` · high. Sim-only (CoppeliaSim, RLBench objects); real world appears only as future work: "the simulation environment, while high-fidelity, does not yet capture all nuances of real-world contact dynamics … Future work". No hardware section. https://arxiv.org/html/2512.04308
- JUDGEMENT · dex · 2 → 1 · medium. Actions are "predefined skills, manipulation poses, and code generation" from LLM/VLM agents, i.e. primitives on a scripted controller, not learned low-level control.
- JUDGEMENT · failure · `accident` → `accident, adversarial` · medium. Has a "Prompt Attack and Defense Evaluation" section (§V-F/VI-F) with adversarial instructions.
- JUDGEMENT · bottleneck · both → cognition · low (follows from dex 1).
- JUDGEMENT · avail · paper → announced · low. "All scenarios used in the experiments will be released."

## homesafe-bench (HomeSafe-Bench)
- ERROR · avail · paper → open · high. Paper header: "Code: https://github.com/pujiayue/HomeSafe-Bench · Dataset: drive.google.com/… · Leaderboard: huggingface.co/spaces/pujiayue/HomeSafe-Bench-Leaderboard". Repo exists (~600 MB). Add `code`.

## safemanip (SafeManip)
- ERROR · avail · paper → open · high. Paper links https://github.com/chengyuehuang511/SafeManip; repo exists (285 MB, pushed 2 Nov 2026). Add `code`.

## annie (ANNIEBench)
- ERROR · code link · `https://github.com/RLCLab/Annie` returns 404 (link check 3 Nov 2026).
- ERROR · avail · open → announced (or paper) · high. Paper: "Code is available at https://github.com/RLC-Lab/Annie" — that repo exists but is empty (size 0, last push Aug 2025). The `code` field's `github.com/RLCLab/Annie` (no hyphen) 404s. https://arxiv.org/html/2509.03383

## safevla (SafeVLA-Bench)
- ERROR · numbers · "9 policy-benchmark entries; 36–56% of successful RoboCasa rollouts violate a clause" → "27 policy–benchmark entries (24 policies); 38–56% of successful RoboCasa-365 rollouts violate a clause" · high. v3 abstract: "evaluating twenty-seven policy–benchmark entries … 38–56% of successful RoboCasa-365 r[ollouts]". The atlas numbers are from v1. https://arxiv.org/abs/2606.00773v3
- ERROR · avail · open → announced · medium. Paper footnote: "Code and data will be released." safevla.org has a leaderboard but links no SafeVLA code or data, only third-party policies.

## vla-arena (VLA-Arena)
- ERROR · summary · "11 task suites, one of which addresses safety" → "11 task suites, five of which make up a Safety dimension (static/dynamic obstacles, cautious grasp, hazard avoidance, state preservation)" · high. §3: "11 task suites organized into four dimensions: Safety, Distractor, Extrapolation, and Long Horizon"; the Safety dimension lists StaticObstacles, CautiousGrasp, HazardAvoidance, StatePreservation, DynamicObstacles. https://arxiv.org/html/2512.22539
- JUDGEMENT · kind · capability → benchmark · low. Close to half the suites are safety suites with cost predicates.

## behavior1k (BEHAVIOR-1K)
- JUDGEMENT · arch · `vla, vlm_agent` → `rl_policy` · medium. The paper evaluates only RL baselines: "We evaluate state-of-the-art reinforcement learning algorithms … with visuomotor control … and action primitives". No VLA or VLM agent is tested. https://arxiv.org/html/2403.09227
- JUDGEMENT · fidelity · `closed_sim` → `closed_sim, real` · low. Has a sim-to-real study on a real Tiago: "We use a real bi-manual mobile manipulator Tiago …" (§6). This affects the g8 real-hardware count.
- ERROR (minor) · venue · "Li et al., CoRL 2022" → "Li et al., 2024 (preliminary version CoRL 2022)" · medium. The linked arXiv 2403.09227 is the 2024 extended paper; arXiv comment: "A preliminary version was published at … CoRL 2022".

## hasard (HASARD)
- INCLUSION · no robotics link: ViZDoom game environments. "While lacking visual fidelity and accurate physics, HASARD effectively mimics real-world navigation and interaction." This is the same category as the removed evaluations that have no robotics link. https://arxiv.org/html/2503.08241
- JUDGEMENT · harm · `local_harm` → [] · low. The entry's own xr reason says "Abstract costs, no real-world harm class".
- ERROR (minor) · venue · "Tomilin et al., 2025" → "Tomilin et al., ICLR 2025" · high (arXiv comment "Accepted to ICLR 2025"). Add `code` https://sites.google.com/view/hasard-bench/.

## egosafety (EgoSafetyBench)
- ERROR (minor) · venue · "Jun 2026" → "Panpatil et al. (AIM Intelligence), Jun 2026" · high (arXiv authors list).
- ERROR (minor) · code · empty → https://github.com/AIM-Intelligence/EgoSafetyBench (dataset: huggingface.co/datasets/AIM-Intelligence/EgoSafetyBench). Linked from the paper header; avail `open` confirmed.

## asimov (ASIMOV Benchmark)
- JUDGEMENT · domain · `household, healthcare` → `household` (or `household, general`) · medium. The healthcare link comes from the data source (NEISS hospital injury reports: "human injury reports from hospitals"). The scenarios are everyday injuries, not robots in healthcare settings.

## homesafe-inspect (HomeSafeBench inspection)
- JUDGEMENT · cx · 2 → 3 · medium. Free exploration of whole VirtualHome houses ("navigates a fully interactive 3D home") fits rubric 3, "multi-room". The entry's own reason says "active exploration over many steps".

## tsha (TSHA)
- ERROR? · avail · open → paper · medium. The paper contains no code or data link (no github/HF href in the HTML) and no release statement beyond "current release" of annotations. GitHub search was rate-limited, so this is unverified.

## agentsafe (AgentSafe / SAFE)
- ERROR? · avail · open → paper · medium. No code or data link anywhere in the full text.
- ERROR? · venue · "CVPR 2026" · low. Neither the paper text nor the arXiv metadata mentions CVPR. Verify, or drop to "Ying et al., Jun 2025".

## attackvla (AttackVLA)
- ERROR? · avail · open → paper · medium. No code link in the full text or arXiv metadata.
- ERROR (minor) · venue · "Nov 2025" → "Li et al., Nov 2025" · high.

## isbench (IS-Bench)
- ERROR (minor) · venue · "AAAI 2026" → "Lu et al., AAAI 2026" · high for the author. AAAI not confirmed in the text (low).

## besafe (BeSafe-Bench)
- JUDGEMENT · numbers · "best agent safe on under 40%" → "best agent completes under 40% of tasks safely" · low. Paper: "even the best-performing agent attains a success-and-safe rate of below 40%". As worded, the atlas line reads as safety coverage, which the paper puts under 60%.
- JUDGEMENT · summary · "the VLA domain uses LIBERO" → "uses VLA-Arena (on LIBERO)" · low. "we adopt VLA-Arena … which extends the LIBERO simulation environment".

## Minor code-field gaps (avail already `open`; add the link)
- libero-plus: https://github.com/sylvestf/LIBERO-plus
- vlatest: https://github.com/ma-labo/VLATest
- foresight-bench: https://github.com/Beijing-AISI/ForesightSafety-Bench

## safestage
- ERROR · avail: `announced` → `open` · high · The repo github.com/JinzhuLuo/SafeStage holds src/, data/, scenes and a pip package. README: "92 tabletop manipulation scenes with 276 English prompts". Last pushed 29 Oct 2026.
- ERROR (minor) · numbers: "Cosmos policy" → "Cosmos3 Nano Policy" · high · §5: "π0.5, GR00T N1.7, DreamZero, and Cosmos3 Nano Policy". The paper says 97 tasks and the released repo has 92 scenes. Keep 97 (the paper's figure), or note the difference.

## robogate
- ERROR · numbers: "50,000+ runs" → "40,000+ experiments (20k uniform + 10k boundary sampling, plus cross-robot runs)" · medium · Abstract: "across 40,000+ total experiments". The only source for "50K+" is the arXiv comment, which describes the failure-pattern dataset (https://arxiv.org/abs/2603.22126).
- ERROR · avail: `paper` → `open` (data) · medium · Paper: "RoboGate is open-source at https://github.com/liveplex-cpu/robogate … failure dictionary … https://huggingface.co/datasets/liveplex/robogate-failure-dictionary". The HF dataset returns 200, but the GitHub repo returns 404 from the API. Set code to the HF dataset.

## industryeqa
- ERROR · code: "" → https://github.com/JackYFL/IndustryEQA (data: huggingface.co/datasets/IndustryEQA/IndustryEQA) · high · Both links are in the abstract footnote.
- ERROR · venue: "Li et al., 2025" → "Li et al., NeurIPS 2025 D&B" · medium · The repo description reads "[NeurIPS 2025 D&B] IndustryEQA".

## humanoid-orch
- ERROR · venue: → "Bajrami et al., CBS 2026" · medium · arXiv comment: "8 pages, CBS 2026".
- JUDGEMENT · fidelity: `qa` → `qa` + `closed_sim` (preliminary) · low · "the simulation layer [is evaluated] in a preliminary replication", which "reproduces the model ranking".

## health-attendant
- ERROR · fidelity: `closed_sim` → `open_loop` · high · §2.3: "Rather than evaluating physical robot behavior, we focused exclusively on the action plans generated…". "A mock server received the LLM's response and returned a simulated execution acknowledgment." Nothing is physically simulated. Change "in simulation" in the summary to "against a mock execution server".
- ERROR · avail: `paper` → `open`; code → https://github.com/kztakemoto/RHASafety · high · Appendix A: "The datasets and code used in this study are publicly available". The repo exists.
- ERROR · venue: → "Nakao, Takemoto, R. Soc. Open Sci. 2026" · high · journal_ref: "R. Soc. Open Sci. (2026) 13 (9): 261022".

## drone-physical
- ERROR · venue: "Tang et al., 2024" → "Tang et al., Communications of the ACM 2026" · high · arXiv journal_ref.
- JUDGEMENT · harm: `infrastructure` → `violence`, `local_harm` (drop `infrastructure`) · low · The atlas label is "Infrastructure & fleet capture". A drone that strikes infrastructure is violence or local harm; it does not capture anything.

## robopair
- ERROR · domain: remove `drone` · high · No drone is tested. The targets are NVIDIA Dolphins (a self-driving VLM), Clearpath Jackal (UGV) and Unitree Go2 (quadruped). The full text contains no "drone" or "quadcopter".
- ERROR (low) · venue: "Robey et al., 2024" → "Robey et al., ICRA 2025" · low · From memory; arXiv lists no journal_ref.

## blindfold
- ERROR · venue: → "Huang et al., ACM SenSys 2026" · high · arXiv comment: "officially accepted for ACM SenSys 2026".

## shawshank
- JUDGEMENT · fidelity: `closed_sim` → `open_loop` · medium · §IV: "Indirect environmental injections are simulated by compositing texts onto RGB frames … outputting task plans as JSON". Success is judged by GPT-4o on the plan. AI2-THOR frames are single captured images, and no closed-loop rollout is scored.
- ERROR · code: "" → https://anonymous.4open.science/r/Shawshank-5058 · medium · Stated in §IV.

## patch-rokae
- ERROR · fidelity: `real` → `closed_sim` + `real` · high · "All evaluations are performed on the LIBERO benchmark" (main results, Table I). The ROKAE arm appears only in one "Physical attack evaluation" subsection. The summary should say the main results come from LIBERO.
- ERROR · venue: "Jun 2026" → "Wang et al., IEEE RA-L 2026" · high · arXiv comment: "Accepted by IEEE Robotics and Automation Letters, 2026"; first author Xiaofei Wang.

## upa-rfas
- ERROR · avail: `paper` → `open`; code → https://github.com/yuyi-sd/UPA-RFAS · high · The repo is linked in the paper and exists.
- ERROR · venue: "Nov 2025" → "Lu et al., CVPR 2026" · high · arXiv comment: "Accepted by CVPR 2026"; first author Hui Lu.

## radeis
- JUDGEMENT · fidelity: `closed_sim` → `qa` (or `open_loop`) · medium · README: "a robot rides a moving platform through a loop of test stations … captures the FPV frame, runs it through your model, records the chosen action". The model's action is never executed, so the loop is not closed (https://github.com/VicOne-OSS-TW/labr7-radeis-InSimPhysicalAI).
- JUDGEMENT · dex: 1 → 0 · medium · Same evidence: the action is not executed.
- JUDGEMENT · domain: `industrial` → add `household`, `healthcare` · low · README scenes: "Patrol Loop, Warehouse, Bookstore, Hospital, or Small House".

## infectbot
- ERROR · fidelity: `open_loop` → `closed_sim` · medium-high · §4.1: "All experiments are conducted using NVIDIA Isaac Sim 4.5.0 and Isaac Lab 2.1 … each atomic operation via standard ROS 2 … dispatch[ed] to the robot side control stack". Ethics statement: "all experiments are confined to compliant simulation environments with no physical deployment".
- ERROR · venue: → "Huang et al., IJCAI 2026" · high · arXiv comment.
- JUDGEMENT · harm: consider adding `local_harm` · low · The evaluation covers "dereliction of duty, privacy compromise, and public safety hazards".

## comms-attacks
- ERROR · fidelity: `open_loop` → `closed_sim` · medium-high · §V-A1: "All experiments are conducted using NVIDIA Isaac Sim 4.5.0 … Isaac Lab 2.1.0". Real-robot validation is listed as future work (§VI-D2).

## rctf2 (gaps g2/g8 cite this entry)
- ERROR · fidelity: `real` → `closed_sim` (containerised robot software / firmware images) · medium-high · §2.2: "CTF and other hands-on exercises run in isolated Docker containers". Fig. 2 places "RCTF2" under "Docker Containers". The paper never says physical robots were attacked. The summary "on real robot platforms" should read "against containerised MiR, UR, xArm and Otto software" (https://arxiv.org/abs/2510.24317).
- ERROR · avail: `open` → `restricted` (commercial) · high · CAI benchmarks README: "Categories Jeopardy-style CTFs, Attack–Defense CTF, and Cyber Range Exercises are available in the CAI PRO version". RCTF2 is a Jeopardy CTF. The public repo's benchmarks/ folder holds only cti_bench, cyberPII-bench, cybermetric and seceval. Table 11 marks the MiR and Otto challenges "Internal".
- ERROR (minor) · numbers: "agents solve 22%" → "best agent (alias1) solves 22% (6 of 27)" · high · §3.2.3.

## icat
- ERROR · venue: "Lai et al., 2026" → "Lai et al., NeurIPS 2026" · high · arXiv comment: "Accepted to NeurIPS 2026 (Poster)".

## robotrust
- ERROR · avail: `paper` → `open`; code → https://huggingface.co/datasets/Huiqiong0124/RoboTrustBench_Dataset · high · The project page (huiqiongli.github.io/RoboTrustBench) links the dataset, which returns 200.
- ERROR · venue: → "Li et al., EMNLP 2026 Findings" · high · arXiv comment.

## labsafety (gap g7 cites this entry)
- INCLUSION · medium · The paper measures LLM/VLM safety knowledge for *human* lab work ("LLMs and VLMs now assist in experiment design and procedural guidance"). No robot or embodied agent is involved. On robotics link it is comparable to LAB-Bench, which was removed. If kept, g7 still holds.
- ERROR · venue: "Zhou et al., 2024" → "Zhou et al., Nature Machine Intelligence 2026" · high · journal_ref: "Nat Mach Intell 8, 20-31 (2026)".
- ERROR · code: "" → https://github.com/YujunZhou/LabSafety-Bench · high.
- ERROR (minor) · numbers: "Text and image QA" → "765 MCQs (text and image), 404 scenarios, 3,128 open-ended tasks" · high · Abstract.

## abc-bench (gaps g2/g7 cite this entry)
- JUDGEMENT · xr: 3 → 2 · medium · Only the liquid-handling task was executed physically, and the paper calls it a benign task: "evaluates LLM agents on both benign and dual-use biology tasks". It is a Gibson assembly of a non-hazardous target. The dual-use components (fragment design, screening evasion) are purely digital. On the rubric, the physically executed part is a precursor capability, not "a catastrophic capability carried through to physical execution". **If accepted, g2's "ABC-Bench is the only surveyed work that measures a catastrophic capability through to physical execution" breaks, and no entry would score xr 3.**
- JUDGEMENT · fidelity: `real` → `open_loop` + `real` · low-medium · The benchmark grades scripts with the "OpenTrons simulation tool". Real execution is limited to "three wet-lab validation experiments".
- ERROR · venue: "Jun 2026" → "Liu et al. (SecureBio), ICML 2026" · high · arXiv comment: "To be published in ICML 2026".

## autobio
- ERROR · code: "" → https://github.com/autobio-bench/AutoBio (models/data: huggingface.co/autobio-bench) · high · The paper header reads "Repo: github.com/autobio-bench/AutoBio".
- ERROR (minor) · venue: "ICLR 2026" → "Lan et al., ICLR 2026" · low · arXiv does not confirm ICLR; worth verifying.

## labvla (gap g7 cites this entry)
- ERROR · summary: "Evaluates VLAs on laboratory tasks composed of two to four atomic skills" → "Proposes LabVLA, a laboratory VLA model, and RoboGenesis, a simulated data engine. It is evaluated on LabUtopia (six operations) and on four real-Franka tasks of 2–4 skills" · high · Abstract and §4–5.2.
- INCLUSION · medium · This is a model and data paper. Its only reusable measure is LabUtopia, which already has its own entry. The four real tasks are ad hoc.
- ERROR · avail: `paper` → `open`; code → https://github.com/zjunlp/LabVLA · high · The repo and HF model exist.
- ERROR · venue: "2026" → "Ren et al., 2026" · high.

## labutopia
- JUDGEMENT · arch: `vla` → no exact tag · low · The baselines are ACT and Diffusion Policy, which are imitation policies with no language input. ACT is mentioned 25 times, Diffusion Policy 8 times, OpenVLA/π0 never.

## pipette (gap g7 cites this entry)
- ERROR · avail: `open` → `announced` · medium · The paper's only code link, "Project page: https://github.com/hbhuiyou/Pipette", returns 404 (web and API).
- ERROR · numbers: "ACT 60.3%" is not in the paper (v3) · medium · The abstract gives SmolVLA 40.4→71.8% and π0 37.3→44.1%. The ACT figures are per category (e.g. 59.5→69.3% on sample/culture tasks). Replace ACT 60.3% with π0 37.3→44.1%.

## refuses-asked
- ERROR (minor) · venue: → "Grover, SPAIS workshop (CoRL 2026) submission" · high · arXiv comment.
Other fields match: 0 of 15 refused, 27% (4) completed, the check stops 15/15 and flags 0/15 controls, SO-101, GPT-6 Astra: all match.

## capsafe
- ERROR · venue: → "Farag et al., REALM 2026" · high · journal_ref.
- JUDGEMENT (gap g4 wording only) · low · CAPSafe's gap is recognition vs **long-horizon planning** in a text-based simulator that "approximates AI2-THOR execution while abstracting away navigation" (supports `open_loop`), not executed action. Entry fields otherwise verified (code github.com/Youmna-H/CAPSafe, 78.19%).

## tapdreamer
- **ERROR, fidelity**: current `closed_sim`, proposed `closed_sim, real`. Confidence high. The paper says: "We further validate TAPDreamer in real-world deployment on an SO-101 robot, with representative FastWAM executions shown in Figure 2" (§ results; "Real-world setup. We additionally evaluate FastWAM and DreamWAM on an SO-101 robot"). Source: https://arxiv.org/abs/2610.06814 (v3). **This breaks g6** ("in simulation (TAPDreamer) and on a physical robot (PASA-KV)"), and the g8 real-hardware count goes from 24 to 25.
- numbers: "97.7%" is 97.65% in the paper, which is fine as rounding. Random patches retain 81.45% and 79.20%; "about 80%" is fine.
- avail/code: the project page is tapdreamer.github.io but links no code. `paper` stays.

## labference
- **ERROR, avail/code**: current `paper` with code empty, proposed `open` with code `https://github.com/LabBuddy26/Labference`. Confidence high. The PDF header reads "Project page: https://github.com/LabBuddy26/Labference" (v2, 2 Nov 2026). The repo is populated (tasks/, evaluation/, robots/, LICENSE, DATASET_LICENSE.md; pushed 2026-11-03).
- JUDGEMENT, dex: current 3, proposed 2. Confidence low. The initial evaluations are weighing and transfer pick-place on a tabletop, which is not contact-rich, bimanual, precision or whole-body.

## dexbiolab
- **ERROR, avail/code**: current `paper` with code empty, proposed `open` with code `https://github.com/CumulusAlpha/DexBioLab`. Confidence high. The PDF links the project page https://cumulusalpha.github.io/DexBioLabWebPage/, which links the GitHub repo (src/, scripts/, pyproject) and the HF dataset `22364yiqun/DexBioLab` (public, CC-BY-4.0).

## embodiedlab
- **ERROR, harm**: current `bio_uplift`, proposed none (or a non-bio precursor tag). Domain `lab_bio` is borderline. Confidence medium-high. The 30 experiments are "in mechanics, electricity, optics, thermal physics and chemistry on 14 apparatus platforms, operated by a robot arm with a two-finger gripper"; there is no biology. Source: https://arxiv.org/abs/2610.35385. The xr reason "precursor for experimental uplift" then has no bio pathway; xr 1 is fine either way. g7 lists it among laboratory works, which still holds, because g7 does not claim bio.

## inspect-robots
- JUDGEMENT, dex: current 2 ("Real arms under model control"), proposed 1. Confidence medium. The LLM policies act only through "Robot control tools, such as move_joints and move_to … Each tool call generates a sequence of actions" (§3). That is abstract primitives on a scripted controller, with no learned low-level control. The demo embodiment is an I2RT YAM bimanual arm (§4). This affects the g3 count (see the bottom of this file).
- JUDGEMENT, fidelity: current `closed_sim, real`. Confidence low. The demonstrated evaluations are real-hardware only ("We run each evaluation on the embodiment yam_arms … I2RT YAM bimanual robot"). Sim is supported by the framework but not shown. Keep it if fidelity describes capability.
- Verified: "nearly 100,000 downloads in the three months since its release [8]", and [8] is PyPI Stats, accessed 1 Oct 2026. PyPI counts include mirrors and CI, so keep g8's "the authors report" attribution. The six safety-eval models are Astra, GPT-6 Sol, GPT-5.6 Sol, Fable 5.1, Opus 5.5 and Gemini 3.8 Flash; the capability eval uses 5 models. Correction to g8's phrasing: Inspect Robots ran a 4-task mini-benchmark *drawn from* RoboHarm. Whether RoboHarm itself uses Inspect Robots as its harness has to be checked in the RoboHarm entry, which is outside this part.

## l3-bench
- **ERROR, fidelity**: current `open_loop`, proposed none or empty. No evaluation of any kind is run. Confidence high. From the full text (§1): "End-to-end LAM training, cross-device transfer experiments, and systematic hardware and safety validation remain to be completed; improvements … are hypotheses to be tested through the proposed evaluation." cx 3, dex 3 and cog 2 score a hypothetical protocol. https://arxiv.org/abs/2610.36761
- summary and g7: "The abstract reports no experimental results" is true, but the *paper* reports none either. Strengthen to "The paper reports no experimental results."
- INCLUSION (separate): this is a specification with no measurement, so it is questionable under "someone else could apply that measure". Confidence medium.

## beyond-behaviour
- g4 claim "describes its methods only briefly": weak. Confidence medium. The main text is a 4-page short paper, but Appendix A gives detailed methods: representation extraction, temporal groups, matched controls for image change, metric computation, and the digital-cousin reconstruction of gripper–danger geometry with execution for 8 sim steps. Suggest dropping the clause, or saying "a short paper".
- numbers: "abstract gives no figures" is accurate for the abstract only. The paper reports the models (VLA-JEPA, GR00T N1.7, X-VLA, on LIBERO/SimplerEnv checkpoints) and the videos (RoboShackles, HomeSafe-Bench). Its main result: "the dominant initial response … is movement towards danger" for all three models on RoboShackles. Optional update.

## siren
- ERROR (minor), numbers: current "3× a baseline", proposed "1.86× a random-search baseline". Confidence medium. The paper is internally inconsistent: the abstract says "three times as many attacks", while the intro and contributions say "discovers 1.86x times as many attacks as identified by the random-search baseline … in 35 vulnerable scenarios from SPARK". https://arxiv.org/abs/2610.31923. Verified: a real Unitree G1, and attacks on all seven safety filters.

## assistive-contact
- ERROR (minor), avail/code: current `paper` with code empty, proposed `open` with code `https://anonymous.4open.science/r/Physics-Consistent-Benchmark4HRC-8DBF/`. Confidence medium. The abstract says "Code and benchmark assets are available at" that anonymous URL. Downgrade to `announced` if anonymous links don't count. Numbers verified.

## blackout-freeze
- avail: the paper cites "Code for reproducing our experiments is available at https://anonymous.4open.science/r/…". Same call as assistive-contact (low). The real robot is a WidowX AI on block-in-bowl, 10 trials per condition, which is consistent with `real`.

## maniphysics
- JUDGEMENT, dex: current 3 ("Contact forces are the measure"), proposed 2. Confidence medium. The tasks are standard LIBERO/SimplerEnv tabletop pick-place with a parallel gripper. The rubric scores motor demand, not what is measured.

## reacthuman
- JUDGEMENT, dex: current 2, proposed 1. Confidence medium. The MLLM picks a plan, and "balance and joint torques are delegated to a pre-trained whole-body controller … so scores are attributable to reasoning rather than policy quality". The model under test emits abstract commands. This affects the g3 count.

## robobugbench
- avail: current `open` with code empty, proposed `announced`, unless a URL is found. Confidence medium. The abstract says "We release the corpus, criterion batteries, counterfeit suite and cached telemetry", but the paper (HTML or PDF) contains no repository URL. https://arxiv.org/abs/2610.16369
- JUDGEMENT, kind: current `benchmark` (safety benchmark), proposed `capability`. Confidence low. It measures software-repair capability. The safety-relevant part is the grader audit (counterfeit patches accepted 11/11).

## guardrail-bench
- arch: add `llm_planner`. Confidence medium. The agents are "GPT-4o (VLM) and open-source DeepSeek-V3.2 (LLM)". Code: "released as anonymous supplementary material", so `paper` is OK.
- INCLUSION (low): it evaluates guardrails, which are mitigations, but frames them as a reusable measure. Probably fine.

## east
- arch (low): the policies are ACT and RDT. ACT is a non-language imitation policy, not a VLA, so `vla` is only half right. The vocab has no imitation-policy tag; consider a note.

## simuguard
- INCLUSION (separate category), medium: it audits simulator contact artefacts in benchmarks and measures no safety-relevant behaviour (failure and harm are empty; the xr reason says "Measures the instrument, not a risk"). It is cited in g8 as context, so if it is kept, it is as a methods note. Numbers verified: 12 in 100 to 0, 89% to 98%, and 83.1% spanning 75.8–98.5%.

## trust-cot
- INCLUSION (low): it is mostly a mitigation (a value model that steers CoT), with eval axes defined around it. Half of its numbers come from Alpamayo 1.5, a driving VLA in AlpaSim, and driving is excluded. Numbers verified: 75.9% to 90.0%, and −30.4% collisions.

## no-instruction (VLAs Do Not Know When Not to Act)
- ERROR · avail/code · `open`, https://github.com/zebehn/vla-start-suppression → `announced` (or `paper`) · high · The paper says "The evaluation code, the episode records … and an evaluation kit … are released at https://github.com/zebehn/vla-start-suppression", but the URL returns 404 and the repo is not in zebehn's public repo list (checked 3 Nov 2026). Other fields verified.

## Verified with no finding
osma-bench, refusals-bend, visual-grounding, goal-misgen, negabench, limits-assurance, rt-safe, pasa-kv (real Piper arm; code "coming soon"), worldfailbench, lie-rarely, industrial-backdoor, roboworld, labshield ("32 models" = 20+9+3; "full dataset will be released soon" confirms `announced`), roboharm (all g4 figures match: 73% text, 18–25% robot, 18% of 612 real EEF trials vs 19% sim; harness is Inspect Robots, ref [29]).

- g6 "seven world models" and "real G1 tasks" are verified: "real-world manipulation tasks performed by the G1 humanoid robot. Experiments across seven world models".
- g1 and g8 Limits of Statistical Assurance are verified: 34 of 36, 12.00 to 3.81 per 24 tasks, and "external language-model controller given an adversarial objective also infers hidden certification from noisy evaluation receipts".
- g5 What Happens to the Goal? is verified: 3 Procgen, 4 arm and 1 ANYmal quadruped (Isaac Lab) tasks, using its own RL policies with no frontier models; the numbers (16.0→95.3, 31.6→84.3) match.
- g9 RoboWorld is verified: 25 test and 175 training environments, and best models get 0% with mean reward 0.06.