# Output index

Every file shipped in the three output folders, with what it contains. All files are aggregate results; no patient-level data are included.

| Folder | Produced by | Configuration |
|---|---|---|
| `nb1_outputs_adm/` | Notebook 1 | Exploratory 6-hour anchor (the setting in the committed notebook) |
| `nb2_outputs/` | Notebook 2 | 24-hour anchor (the reported analysis) |
| `nb3_outputs/` | Notebook 3 | 24-hour anchor (the reported analysis) |

## `nb1_outputs_adm/`

| File | Contents |
|---|---|
| [`figures/fig_consort_flow.png`](../nb1_outputs_adm/figures/fig_consort_flow.png) | Cohort derivation and analysis flow (PNG; vector PDF alongside) |
| [`figures/fig_correlation_heatmap.png`](../nb1_outputs_adm/figures/fig_correlation_heatmap.png) | Feature correlation heatmap (PNG; vector PDF alongside) |
| [`figures/fig_feature_violins.png`](../nb1_outputs_adm/figures/fig_feature_violins.png) | Feature distributions by database (PNG; vector PDF alongside) |
| [`figures/fig_missingness_heatmap.png`](../nb1_outputs_adm/figures/fig_missingness_heatmap.png) | Missingness patterns (PNG; vector PDF alongside) |
| [`figures/fig_outcome_treatment_rates.png`](../nb1_outputs_adm/figures/fig_outcome_treatment_rates.png) | Outcome and treatment rates by database (PNG; vector PDF alongside) |
| [`figures/fig_sofa_distribution.png`](../nb1_outputs_adm/figures/fig_sofa_distribution.png) | SOFA distributions by database (PNG; vector PDF alongside) |
| [`nb1_manifest.json`](../nb1_outputs_adm/nb1_manifest.json) | Run manifest: inputs, outputs and settings |
| [`nb1_run.log`](../nb1_outputs_adm/nb1_run.log) | Run log with timings and headline numbers |
| [`tables/data_quality_summary.csv`](../nb1_outputs_adm/tables/data_quality_summary.csv) | Stays, mortality, age, SOFA, organ support and missingness by database |
| [`tables/eicu_consort.csv`](../nb1_outputs_adm/tables/eicu_consort.csv) | Cohort derivation steps and counts, eICU-CRD |
| [`tables/feature_dictionary.csv`](../nb1_outputs_adm/tables/feature_dictionary.csv) | Every analytic variable with its role, type and missingness |
| [`tables/mcar_tests.csv`](../nb1_outputs_adm/tables/mcar_tests.csv) | Tests of missing-completely-at-random by feature |
| [`tables/mice_sensitivity.csv`](../nb1_outputs_adm/tables/mice_sensitivity.csv) | Agreement between multiple imputation and median imputation |
| [`tables/mimic_consort.csv`](../nb1_outputs_adm/tables/mimic_consort.csv) | Cohort derivation steps and counts, MIMIC-IV |
| [`tables/missingness_by_database.csv`](../nb1_outputs_adm/tables/missingness_by_database.csv) | Missingness of each feature in MIMIC-IV and eICU-CRD |
| [`tables/table1_baseline_characteristics.csv`](../nb1_outputs_adm/tables/table1_baseline_characteristics.csv) | Baseline characteristics by database and survival |

## `nb2_outputs/`

| File | Contents |
|---|---|
| [`figures/fig_ate_cate.png`](../nb2_outputs/figures/fig_ate_cate.png) | Average effect estimates and distribution of individual effects (the interval drawn on the DR-ATO row belongs to the g-formula row; use ate_estimates.csv) (PNG; vector PDF alongside) |
| [`figures/fig_attributions.png`](../nb2_outputs/figures/fig_attributions.png) | Risk-model and propensity attributions (exploratory) (PNG; vector PDF alongside) |
| [`figures/fig_audit_operating_characteristic.png`](../nb2_outputs/figures/fig_audit_operating_characteristic.png) | Semi-synthetic benchmark: audit recovery versus c-for-benefit (PNG; vector PDF alongside) |
| [`figures/fig_decision_curves.png`](../nb2_outputs/figures/fig_decision_curves.png) | Classical decision curve versus prescriptive net-harm curve (PNG; vector PDF alongside) |
| [`figures/fig_deployment_safety_curves.png`](../nb2_outputs/figures/fig_deployment_safety_curves.png) | Net expected excess deaths across thresholds (internal and external), harm rates and decision stability (PNG; vector PDF alongside) |
| [`figures/fig_discrimination_calibration.png`](../nb2_outputs/figures/fig_discrimination_calibration.png) | ROC (internal), precision-recall (external) and calibration of the primary model (PNG; vector PDF alongside) |
| [`figures/fig_inversion_disagreement.png`](../nb2_outputs/figures/fig_inversion_disagreement.png) | Benefit-risk inversion and policy-versus-care disagreement matrix at the reference threshold (PNG; vector PDF alongside) |
| [`figures/fig_love_balance.png`](../nb2_outputs/figures/fig_love_balance.png) | Covariate balance before and after overlap weighting (PNG; vector PDF alongside) |
| [`figures/fig_pdp_ice_treatment.png`](../nb2_outputs/figures/fig_pdp_ice_treatment.png) | Partial dependence on age and distribution of the treatment influence (PNG; vector PDF alongside) |
| [`figures/fig_propensity_overlap.png`](../nb2_outputs/figures/fig_propensity_overlap.png) | Propensity score overlap for post-anchor organ support (PNG; vector PDF alongside) |
| [`figures/fig_subgroup_forest.png`](../nb2_outputs/figures/fig_subgroup_forest.png) | Audit by sex, race group and age band (PNG; vector PDF alongside) |
| [`figures/fig_waterfall_sankey.png`](../nb2_outputs/figures/fig_waterfall_sankey.png) | Excess-deaths waterfall and treated-patient flow at the reference threshold (bars clipped) (PNG; vector PDF alongside) |
| [`nb2_manifest.json`](../nb2_outputs/nb2_manifest.json) | Run manifest: inputs, outputs and settings |
| [`nb2_run.log`](../nb2_outputs/nb2_run.log) | Run log with timings and headline numbers |
| [`tables/ablation_mitigation.csv`](../nb2_outputs/tables/ablation_mitigation.csv) | Audit with and without surrogate features |
| [`tables/alternative_rules_compliance.csv`](../nb2_outputs/tables/alternative_rules_compliance.csv) | Threshold-by-threshold audit metrics, with clinician compliance of 100%, 75%, 50% and 25% |
| [`tables/ate_estimates.csv`](../nb2_outputs/tables/ate_estimates.csv) | Average treatment effect of organ support: g-formula, IPW, MSM, AIPW, overlap-weighted DR |
| [`tables/audit_validity_floor.json`](../nb2_outputs/tables/audit_validity_floor.json) | Benchmark c-for-benefit floor and observed values |
| [`tables/cate_learner_validation.csv`](../nb2_outputs/tables/cate_learner_validation.csv) | c-for-benefit and benefit distribution for S-, T-, X- and DR-learners |
| [`tables/covariate_balance.csv`](../nb2_outputs/tables/covariate_balance.csv) | Standardised mean differences for key covariates before and after weighting |
| [`tables/covariate_balance_full.csv`](../nb2_outputs/tables/covariate_balance_full.csv) | Standardised mean differences for all 324 encoded covariates |
| [`tables/delong_tests.csv`](../nb2_outputs/tables/delong_tests.csv) | Paired AUROC comparisons (see note in the README) |
| [`tables/evalue.json`](../nb2_outputs/tables/evalue.json) | E-value for the average effect |
| [`tables/fdr_sweep.csv`](../nb2_outputs/tables/fdr_sweep.csv) | Threshold-wise permutation tests with Benjamini-Hochberg correction |
| [`tables/headline_ci.csv`](../nb2_outputs/tables/headline_ci.csv) | Bootstrap intervals for the primary PSS and DHI |
| [`tables/importance_risk_model.csv`](../nb2_outputs/tables/importance_risk_model.csv) | Permutation importance for the risk model (small sample, exploratory) |
| [`tables/modality_audits.csv`](../nb2_outputs/tables/modality_audits.csv) | Audit for vasopressors, ventilation, renal replacement therapy and the composite |
| [`tables/model_performance.csv`](../nb2_outputs/tables/model_performance.csv) | AUROC (95% CI), AUPRC, Brier, ECE, MCC and log loss for five models, internal and external |
| [`tables/positivity_overlap.json`](../nb2_outputs/tables/positivity_overlap.json) | Propensity overlap diagnostics |
| [`tables/prescriptive_safety_scores.csv`](../nb2_outputs/tables/prescriptive_safety_scores.csv) | PSS, DHI, CAR and risk-benefit concordance for each model and cohort |
| [`tables/risk_treatment_overlap.json`](../nb2_outputs/tables/risk_treatment_overlap.json) | Overlap of top risk and treatment drivers |
| [`tables/robustness_battery.csv`](../nb2_outputs/tables/robustness_battery.csv) | Audit under prevalence resampling, added missingness and recalibration |
| [`tables/semisynthetic_operating_characteristic.csv`](../nb2_outputs/tables/semisynthetic_operating_characteristic.csv) | Benchmark: c-for-benefit and recovery of the true DHI at 12 noise levels |
| [`tables/semisynthetic_recovery.csv`](../nb2_outputs/tables/semisynthetic_recovery.csv) | Benchmark replicate-level results |
| [`tables/semisynthetic_validation.csv`](../nb2_outputs/tables/semisynthetic_validation.csv) | Earlier benchmark variant (superseded by the operating-characteristic table) |
| [`tables/subgroup_prescriptive_safety.csv`](../nb2_outputs/tables/subgroup_prescriptive_safety.csv) | Audit by sex, race group and age band |
| [`tables/tii_summary.json`](../nb2_outputs/tables/tii_summary.json) | Treatment Influence Index and AUROC with and without treatment |

## `nb3_outputs/`

| File | Contents |
|---|---|
| [`cate_bootstrap.npz`](../nb3_outputs/cate_bootstrap.npz) | DHI from 40 bootstrap refits of the effect model (no patient data) |
| [`figures/fig_benefit_validation.png`](../nb3_outputs/figures/fig_benefit_validation.png) | Benefit distribution and calibration for benefit (smoother line uninformative; use decile points) (PNG; vector PDF alongside) |
| [`figures/fig_causal_dag.png`](../nb3_outputs/figures/fig_causal_dag.png) | Assumed causal structure (PNG; vector PDF alongside) |
| [`figures/fig_consolidated_robustness.png`](../nb3_outputs/figures/fig_consolidated_robustness.png) | Robustness scenarios, transportability and subgroups (PNG; vector PDF alongside) |
| [`figures/fig_consort_flow.png`](../nb3_outputs/figures/fig_consort_flow.png) | Cohort derivation and analysis flow (PNG; vector PDF alongside) |
| [`figures/fig_graphical_abstract.png`](../nb3_outputs/figures/fig_graphical_abstract.png) | Early summary plot of PSS versus counterfactual agreement (title overstates the spread; models cluster) (PNG; vector PDF alongside) |
| [`figures/fig_negative_controls.png`](../nb3_outputs/figures/fig_negative_controls.png) | Negative-control analyses (PNG; vector PDF alongside) |
| [`figures/fig_permutation_inference.png`](../nb3_outputs/figures/fig_permutation_inference.png) | Permutation nulls for the DHI (PNG; vector PDF alongside) |
| [`figures/fig_quantitative_bias_analysis.png`](../nb3_outputs/figures/fig_quantitative_bias_analysis.png) | Bias-adjusted risk ratio across confounder strengths (PNG; vector PDF alongside) |
| [`figures/fig_study_design.png`](../nb3_outputs/figures/fig_study_design.png) | Landmark design and audit pipeline (original schematic) (PNG; vector PDF alongside) |
| [`figures/fig_tipping_point.png`](../nb3_outputs/figures/fig_tipping_point.png) | Tipping-point analysis (degenerate in this run) (PNG; vector PDF alongside) |
| [`figures/fig_uncertainty.png`](../nb3_outputs/figures/fig_uncertainty.png) | DHI across effect-model refits; bootstrap HRR and EED at the reference threshold (PNG; vector PDF alongside) |
| [`manuscript/abstract.md`](../nb3_outputs/manuscript/abstract.md) | Auto-generated draft summary written by Notebook 3 |
| [`manuscript/figure_captions.md`](../nb3_outputs/manuscript/figure_captions.md) | Auto-generated figure captions |
| [`manuscript/limitations.md`](../nb3_outputs/manuscript/limitations.md) | Auto-generated limitations |
| [`manuscript/results_narrative.md`](../nb3_outputs/manuscript/results_narrative.md) | Auto-generated results narrative |
| [`nb3_manifest.json`](../nb3_outputs/nb3_manifest.json) | Run manifest: inputs, outputs and settings |
| [`nb3_run.log`](../nb3_outputs/nb3_run.log) | Run log with timings and headline numbers |
| [`supplementary/abbreviations.csv`](../nb3_outputs/supplementary/abbreviations.csv) | Abbreviations used in the outputs |
| [`supplementary/reproducibility_report.json`](../nb3_outputs/supplementary/reproducibility_report.json) | Seed, platform, package versions, cohort sizes and headline numbers |
| [`supplementary/reviewer_response_matrix.csv`](../nb3_outputs/supplementary/reviewer_response_matrix.csv) | Same, as CSV |
| [`supplementary/reviewer_response_matrix.md`](../nb3_outputs/supplementary/reviewer_response_matrix.md) | Anticipated methodological criticisms mapped to the analyses that address them |
| [`supplementary/tripod_ai_checklist.csv`](../nb3_outputs/supplementary/tripod_ai_checklist.csv) | Mapping of the analysis to TRIPOD+AI reporting domains |
| [`tables/all_main_tables.xlsx`](../nb3_outputs/tables/all_main_tables.xlsx) | All main tables in one workbook |
| [`tables/benefit_calibration.csv`](../nb3_outputs/tables/benefit_calibration.csv) | Predicted versus observed benefit by decile (descriptive) |
| [`tables/benefit_calibration_metrics.json`](../nb3_outputs/tables/benefit_calibration_metrics.json) | Calibration error for benefit |
| [`tables/benefit_gate.csv`](../nb3_outputs/tables/benefit_gate.csv) | Nearest-neighbour c-for-benefit with bootstrap CI (better-than-random criterion) |
| [`tables/c_for_benefit.json`](../nb3_outputs/tables/c_for_benefit.json) | Nearest-neighbour c-for-benefit, internal and external |
| [`tables/negative_controls.csv`](../nb3_outputs/tables/negative_controls.csv) | Negative-control outcomes and sham exposure |
| [`tables/permutation_inference.json`](../nb3_outputs/tables/permutation_inference.json) | Permutation tests for the DHI |
| [`tables/quantitative_bias_analysis.csv`](../nb3_outputs/tables/quantitative_bias_analysis.csv) | Bias-factor grid for unmeasured confounding |
| [`tables/seed_stability.json`](../nb3_outputs/tables/seed_stability.json) | DHI across five random seeds |
| [`tables/subgroup_multiplicity.csv`](../nb3_outputs/tables/subgroup_multiplicity.csv) | Multiplicity-adjusted subgroup tests |
| [`tables/table1_baseline_characteristics.csv`](../nb3_outputs/tables/table1_baseline_characteristics.csv) | Baseline characteristics of the 24-hour landmark cohorts (MIMIC-IV vs eICU-CRD) |
| [`tables/table1_baseline_characteristics.tex`](../nb3_outputs/tables/table1_baseline_characteristics.tex) | LaTeX version of the table of the same name |
| [`tables/table2_model_performance.csv`](../nb3_outputs/tables/table2_model_performance.csv) | Model performance (formatted) |
| [`tables/table2_model_performance.tex`](../nb3_outputs/tables/table2_model_performance.tex) | LaTeX version of the table of the same name |
| [`tables/table2b_delong_tests.csv`](../nb3_outputs/tables/table2b_delong_tests.csv) | Paired AUROC comparisons (formatted; see note in the README) |
| [`tables/table3_prescriptive_safety.csv`](../nb3_outputs/tables/table3_prescriptive_safety.csv) | Prescriptive Safety Audit by model (formatted) |
| [`tables/table3_prescriptive_safety.tex`](../nb3_outputs/tables/table3_prescriptive_safety.tex) | LaTeX version of the table of the same name |
| [`tables/table4_external_validation.csv`](../nb3_outputs/tables/table4_external_validation.csv) | Internal versus external comparison |
| [`tables/table4_external_validation.tex`](../nb3_outputs/tables/table4_external_validation.tex) | LaTeX version of the table of the same name |
| [`tables/table5_sensitivity.csv`](../nb3_outputs/tables/table5_sensitivity.csv) | Sensitivity and ablation analyses (formatted) |
| [`tables/table6_subgroups.csv`](../nb3_outputs/tables/table6_subgroups.csv) | Subgroup audit with bootstrap CIs and adjusted p values |
| [`tables/table6_subgroups.tex`](../nb3_outputs/tables/table6_subgroups.tex) | LaTeX version of the table of the same name |
| [`tables/tipping_point.json`](../nb3_outputs/tables/tipping_point.json) | Tipping-point analysis (degenerate in this run; see README) |
| [`tables/transportability_decomposition.csv`](../nb3_outputs/tables/transportability_decomposition.csv) | Reweighting of eICU-CRD to MIMIC-IV (uninformative: databases perfectly separable) |
| [`tables/uncertainty_propagation.json`](../nb3_outputs/tables/uncertainty_propagation.json) | DHI across effect-model refits; bootstrap HRR and EED at the reference threshold |

## Not included

- Patient-level analytic tables (Parquet), caches, design matrices and trained models.
- `nb2_outputs/tables/failure_cases.csv` and `nb2_outputs/figures/fig_failure_cases.*`, which list individual stays.
- Notebook cell outputs that displayed rows of patient-level tables were cleared; the code in those cells is unchanged.

These exclusions follow the PhysioNet credentialed data use agreement, which does not permit sharing patient-level or derived patient-level data.
