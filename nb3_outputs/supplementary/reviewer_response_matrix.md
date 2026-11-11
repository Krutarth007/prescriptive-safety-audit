# Reviewer stress test: criticism-to-response matrix

| reviewer | anticipated_criticism | response_analysis | artefact |
| --- | --- | --- | --- |
| Causal inference | Treatment effect is confounded by indication | Propensity model, stabilised IPW, MSM, g-formula, and AIPW cross-fitted; overlap and positivity checked | ate_estimates.csv, positivity_overlap.json, fig_propensity_overlap |
| Causal inference | Unmeasured confounding could explain the effect | E-value for the average effect and an additive tipping-point for the prescriptive verdict | evalue.json, tipping_point.json, fig_tipping_point |
| Causal inference | The benefit model may be uninformative here | Correct; c-for-benefit is near 0.5 (hold=0.565), and we quantify exactly when that blinds the audit via a ground-truth operating characteristic | c_for_benefit.json, semisynthetic_operating_characteristic.csv, audit_validity_floor.json, fig_audit_operating_characteristic |
| Methods reviewer | Why trust an audit whose benefit model fails | We do not claim a harm verdict on real data; the contribution is the validity floor and the demonstration that ICU registries fall below it | audit_validity_floor.json, fig_audit_operating_characteristic |
| Senior statistician | Prescriptive harm may be a chance finding | Randomisation inference with benefit- and risk-permutation nulls | permutation_inference.json, fig_permutation_inference |
| Senior statistician | Point estimates lack uncertainty | Bootstrap intervals including treatment-effect-model error; DeLong CIs for AUROC | uncertainty_propagation.json, headline_ci.csv, fig_uncertainty |
| Senior statistician | Pipeline could fabricate effects | Negative-control outcomes immutable to treatment return near-zero adjusted effect | negative_controls.csv, fig_negative_controls |
| Clinical intensivist | The deployment rule is a strawman | Risk-guided de-escalation is the documented behaviour; full threshold sweep reported | fig_deployment_safety_curves, fig_decision_curves |
| Clinical intensivist | Harm must be clinically legible | Expected excess deaths per 1000 and named failure cases with physiology | failure_cases.csv, fig_failure_cases, fig_waterfall_sankey |
| Machine learning | Findings may be specific to one learner | Five model families audited; DeLong comparisons; consistent PSS ordering | table3_prescriptive_safety.csv, table2b_delong_tests.csv |
| Machine learning | Leakage from treatment into features | Landmark design; treatment excluded from covariates; ablation of surrogates | ablation_mitigation.csv, fig_study_design |
| Reproducibility | Results may not transport or reproduce | External eICU validation; fixed seeds; cached artefacts; TRIPOD+AI checklist | table4_external_validation.csv, reproducibility_report.json, tripod_ai_checklist.csv |
| Reproducibility | Calibration drift across sites ignored | Calibration-drift scenario with site recalibration in the robustness battery | robustness_battery.csv, fig_consolidated_robustness |
| Associate editor | Novelty may be overstated | Claim limited to a deployment-evaluation methodology; prediction models are instruments | manuscript/abstract.md, framework definitions in Notebook 2 section 4 |
| Associate editor | Generalisability beyond two US databases | Stated as a residual limitation; audit is dataset-agnostic and released for external use | manuscript/limitations.md |