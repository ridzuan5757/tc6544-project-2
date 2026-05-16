# TC6244 Project 2 — Part B (RL) — Task Breakdown

Each task below is **self-contained** and **independent** — no task waits on another's output. Any member can pick any task, read the cited thesis section, and write the answer in isolation.

## Conventions

- **Source:** `CMU-CS-25-110.pdf` unless noted otherwise.
- **Deliverable per task:** 1–2 page written answer (markdown or LaTeX) with at least one table/figure/equation where useful, plus thesis citations (chapter/section/figure/table number).
- **Independence:** All thesis references and ML concepts needed for each task are listed inline. Do **not** rely on another team member's draft to complete your task.

---

## Task 1 — Q1: Treatment Variation Across Paradigms

**Prompt.** Why is treatment variation important for both reinforcement learning and supervised learning in healthcare?

**Read.**
- Thesis Section 2.1 (RL background), Section 2.1.2 (overlap assumption / causal inference)
- Thesis Section 3.1 (problem formulation for RL in sepsis treatment)

**Cover.**
- RL perspective: counterfactual reasoning, Q-function estimation `Q(s,a)`, policy `π(a|s)`
- SL perspective: treatment as a feature, discriminative signal, feature variability
- Overlap assumption from causal inference (each patient must have nonzero probability of receiving any treatment)
- Failure modes when variation is absent

**Output cues.** A small comparison table (RL vs SL vs Causal Inference) summarising why variation matters in each paradigm.

---

## Task 2 — Q2: Transformers vs RNN/LSTM for Temporal Modelling

**Prompt.** How do transformer-based dynamics models improve temporal modelling compared to RNN or LSTM?

**Read.**
- Thesis Section 3.2.2 (transformer dynamics architecture: 2 blocks, 4 self-attention layers, 16 heads, dim 1024)
- Thesis Figure 3.2 (training/validation loss curves vs RNN baseline)

**Cover.**
- Self-attention `softmax(QK^T / √d_k) V` vs sequential hidden state `h_t = f(h_{t-1}, x_t)`
- Long-range dependencies, parallelisation, training stability, representation capacity
- Multi-head attention (16 heads outperformed 4)
- Multitask training framework (regression + classification objectives) and why it suits transformers
- ICU-specific motivations: multi-scale dynamics, irregular interactions, multivariate coupling

**Output cues.** Architecture comparison table; one paragraph each on stability and parallelisation evidence from Figure 3.2.

---

## Task 3 — Q3: Action Inputs as Feature Importance Analysis

**Prompt.** How does comparing models with and without treatment-action inputs resemble feature importance analysis in supervised learning?

**Read.**
- Thesis Chapter 3 (81 dynamics models trained across 3 groups: States+Actions, States only, Actions only)
- Thesis Figure 3.3 (RMSE comparisons across conditions)

**Cover.**
- Map the three training groups to ablation / leave-one-out / permutation importance
- Test-time interventions: Shuffled → permutation importance; Zero/Mean → drop-column importance
- Connection to SHAP values and partial dependence (behaviour cloning R² in Figure 3.5)
- "Null result" finding: RMSE nearly constant across conditions → actions not predictive in aggregate

**Output cues.** Two-column table mapping SL feature-importance methods to thesis equivalents.

---

## Task 4 — Q4: ΔRMSE as Treatment Relevance Signal (ML + Clinical)

**Prompt.** How can predictive performance differences between action-aware and action-agnostic models signal treatment relevance? Discuss ML and clinical perspectives.

**Read.**
- Thesis Chapter 4 (GridWorld validation; Table 4.2 — 86% accuracy, 0.832 ROC AUC at 1-step horizon)
- Thesis Chapter 5 / Figure 5.3 (treatment heatmaps, AI Clinician comparison)

**Cover.**
- Formal signal: `Δ_RMSE = RMSE(f_no-action) − RMSE(f_action)`
- Interpretation table for Δ_RMSE ≫ 0, ≈ 0, < 0
- ML perspective: action relevance as marginal predictive value; classifier built on error differences
- Clinical perspective: identifying protocol-driven care, targeting clinical decision support, pre-deployment diagnostic, safety boundary
- GridWorld validation evidence (action-diverse 1.42 vs non-diverse 3.59 RMSE)

**Output cues.** One table for the Δ_RMSE interpretation, one short subsection for each of ML and Clinical perspectives.

---

## Task 5 — Q5: Simulation as ML Evaluation Tool

**Prompt.** How does simulation function as an ML evaluation tool and what are its advantages over real-world validation?

**Read.**
- Thesis Chapter 4 (1D GridWorld simulation built on Gymnasium framework)
- Thesis Table 4.1, Table 4.2

**Cover.**
- Simulation design: 20 discrete states, action-diverse vs non-diverse splits, reward ranges
- Advantages over real data: ground truth, controllability, no confounders, reproducibility, cost/ethics, scalability, iteration speed
- Three-stage validation: dynamics model → classifier → robustness across horizons
- Limitations: simplified dynamics, discrete state space, uniform action selection

**Output cues.** Advantages comparison table (Simulation vs Real-World); short pseudocode block of the GridWorld transition rules.

---

## Task 6 — Q6: Replacing Transformers with Random Forest / Gradient Boosting

**Prompt.** How might results differ if transformer-based dynamics models were replaced with Random Forest or Gradient Boosting?

**Read.**
- Thesis Chapter 3 footnote 3 (authors also tested linear + recurrent + XGBoost; transformers won)
- Thesis Chapter 4 (already uses XGBoost in the simulation experiments)

**Cover.**
- Capability comparison: temporal modelling, variable-length sequences, feature interactions, data requirements, interpretability, compute cost
- Expected impacts: (1) decreased sensitivity to delayed action signals, (2) GridWorld results likely preserved, (3) interpretability gain from native feature importance, (4) risk of false negatives on complex temporal pathways
- Anchor the answer to the thesis's own XGBoost-vs-transformer findings

**Output cues.** Capability comparison table; 4-point list of expected impacts on treatment-variation detection.

---

## Task 7 — Q7: Offline RL vs Supervised Learning, and Action Diversity in RL

**Prompt.** How does offline RL differ from supervised learning on the same dataset, and why does action diversity matter more in RL?

**Read.**
- Thesis Section 2.1, Section 3.1 (RL formulation)
- Thesis Section 3.3.3 (behaviour cloning results, low R²)

**Cover.**
- Objective, what is learned, counterfactual requirement, data needs, error propagation, evaluation method
- Q-function `Q(s,a) = E[Σ γ^t r_t | s_0=s, a_0=a]` requires diverse actions in similar states
- Bellman backup `π*(s) = argmax_a [r(s,a) + γ Σ P(s'|s,a) V(s')]` and compounding errors over horizons
- Thesis evidence: SL can predict SOFA equally with/without actions, but RL fails because behaviour cloning shows insufficient action variation

**Output cues.** Side-by-side comparison table (Offline RL vs SL); numbered list of why action diversity matters more in RL.

---

## Task 8 — Q8: t-SNE / UMAP for Treatment-Variation Exploration

**Prompt.** How can t-SNE or UMAP support exploration of treatment variation across patient state spaces?

**Read.**
- Thesis Chapter 5 (interactive visualisation tool)
- Thesis Figure 5.1, 5.2, 5.3 (SOFA clusters, treatment heatmaps)

**Cover.**
- Pipeline: 95-variable patient data → transformer autoencoder (4 encoder layers, 8 heads) → 32-dim latent → t-SNE (cosine) → 2D scatterplot with interactive selection
- How t-SNE supports analysis: cluster identification, treatment pattern visualisation by colour-coding, interactive subgroup selection (lasso → heatmaps + error histograms)
- t-SNE vs UMAP comparison (local/global structure, computational cost, scalability, hyperparameter sensitivity, reproducibility)
- Potential UMAP benefits: better global structure, scalability to 2M timesteps, 3D projections, semi-supervised mode

**Output cues.** Pipeline diagram (text-based OK); t-SNE vs UMAP comparison table.

---

## Task 9 — Q9: Evaluating Model Reliability in Healthcare ML

**Prompt.** How would you evaluate model reliability in healthcare using different machine learning paradigms?

**Read.**
- Whole thesis as context — Chapter 3 (RMSE comparisons), Chapter 4 (classifier validation), Chapter 5 (cluster validation against SOFA)

**Cover.**
- Cross-paradigm framework: Supervised (calibration curves, Brier, prediction intervals), RL (off-policy evaluation, importance sampling, model-based simulation), Causal Inference (overlap diagnostics, sensitivity, refutation tests), Unsupervised (cluster stability, silhouette, clinical validation)
- Multi-level reliability assessment:
  - Level 1 — Data sufficiency (action diversity score, overlap diagnostics, effective sample size)
  - Level 2 — Model performance (AUC-ROC, RMSE, calibration via Hosmer-Lemeshow, uncertainty quantification)
  - Level 3 — Clinical validation (face validity, subgroup analysis, temporal stability / concept drift)
  - Level 4 — Deployment safety (OOD detection, override monitoring, outcome monitoring)
- RL-specific point: OPE methods unreliable when action diversity is insufficient → thesis's Δ_RMSE diagnostic should be applied *before* OPE

**Output cues.** Master table mapping paradigm → reliability metric → clinical interpretation → thesis connection.

---

## Task 10 — Q10: Strategy for Low Treatment Variation (Pick One + Justify)

**Prompt.** To improve policy learning in datasets with low treatment variation, which strategy would you pick: data augmentation, causal inference, representation learning, or simulation-based learning? Why?

**Read.**
- Thesis Chapter 4 (simulation experiments)
- Thesis Chapter 5 (representation learning via autoencoder)
- Thesis Section 2.1.2 (causal inference / overlap)

**Cover.**
- Analysis of each strategy: mechanism, pros, cons, and thesis relevance
- Recommended pick and justification — **simulation-based learning (with caveats)** is the strongest standalone choice because it directly addresses insufficient action diversity, uses the thesis's transformer dynamics as a "world model" to generate counterfactual trajectories
- Integrated pipeline proposal: representation learning (Stage 1) → simulation (Stage 2) → causal constraints (Stage 3) → data augmentation (Stage 4)
- Why other strategies *alone* fall short (augmentation risks unrealistic transitions; causal inference cannot manufacture diversity; representation learning cannot create absent diversity)

**Output cues.** Four-strategy comparison table; final pick boxed/highlighted; multi-stage pipeline diagram.

---

## Task 11 — Q11: Thesis Improvements (Open-Ended Critique)

**Prompt.** How would you improve the thesis? Discuss your suggestions.

**Read.**
- Thesis Section 3.4 (acknowledged limitations)
- Thesis Section 5.4 (discussion / future work)
- Thesis Section 5.3.2 (preliminary peer feedback on visualisation tool)

**Cover.** Propose 5–6 concrete improvements. Suggested seeds:
1. **Multi-domain validation** — extend beyond sepsis (chronic disease, chemotherapy, mental health)
2. **Bridge simulation-to-real gap** — use trained transformer dynamics as an intermediate learned simulator
3. **Temporal attention analysis** — visualise attention patterns to add interpretability over the ablation approach
4. **Multi-centre data** — incorporate eICU (208 hospitals) for cross-institutional variation
5. **Expand action space** — antibiotics, mechanical ventilation, timing of interventions
6. **Formal user study** — structured usability evaluation of the visualisation tool

For each: state current limitation → proposed improvement → expected impact.

**Output cues.** Priority summary table (High / Medium / Lower) at the end.

---

## Task 12 — Integration & Compilation (LaTeX Port)

**Prompt.** Port each notebook into its corresponding `report/Chapters/Question*.tex`, then build the final PDF.

**Inputs.** Each member's completed `question_N.ipynb` (Tasks 1–11) merged into `main`.
**Process.** Notebook → LaTeX porting is done **manually with Claude's help** (not pandoc) so that equations, tables, and citation formatting stay consistent with the existing report style.
**Output.** Updated `report/main.pdf`, cross-checked citations, consistent table style, cover page with all three matric numbers.

> This is the only task with dependencies — it waits on Tasks 1–11.

---

## Quick Assignment View (3 Members × Independent Tasks)

| Task | Member | Status |
|---|---|---|
| Task 1 (Q1) | Member 1 | ☐ |
| Task 2 (Q2) | Member 2 | ☐ |
| Task 3 (Q3) | Member 1 | ☐ |
| Task 4 (Q4) | Member 3 | ☐ |
| Task 5 (Q5) | Member 3 | ☐ |
| Task 6 (Q6) | Member 2 | ☐ |
| Task 7 (Q7) | Member 1 | ☐ |
| Task 8 (Q8) | Member 2 | ☐ |
| Task 9 (Q9) | Member 1 | ☐ |
| Task 10 (Q10) | Member 3 | ☐ |
| Task 11 (Q11) | Member 3 | ☐ |
| Task 12 (Compile) | TBD | ☐ |
