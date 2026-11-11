# Methods in brief

This page summarises the design and every audit quantity. Full detail is in the three notebooks.

## Design

| Element | Definition |
|---|---|
| Data | MIMIC-IV v2.2 (single centre, Boston, 2008 to 2019; development and internal hold-out) and eICU-CRD v2.0 (208 US hospitals, 2014 to 2015; external validation) |
| Population | First ICU stay of adults (18 years or older) still in the ICU 28 hours after admission |
| Decision time (anchor) | 24 hours after ICU admission |
| Covariates L | 177 variables from the first 24 hours: vital signs, laboratory values (minimum, maximum, mean, last), first-day SOFA components, 31 Elixhauser comorbidities, age, sex, race group, admission type, insurance |
| Treatment A | Any vasopressor, mechanical ventilation or renal replacement therapy recorded after the anchor (composite), plus each component separately |
| Outcome Y | In-hospital mortality |
| Split | MIMIC-IV 70:30 at random, stratified by outcome (25,248 development, 10,821 hold-out); eICU-CRD 86,403 stays, external |

The composite treatment mixes initiation with continuation of three therapies. It is a stress test for the audit, not a well-defined clinical intervention. The 28-hour eligibility rule conditions the population on survival and ICU stay for 4 hours after the decision time.

## Prediction models

Logistic regression, random forest, histogram gradient boosting, XGBoost and LightGBM (primary), trained on L only, each wrapped in isotonic calibration (3-fold). Preprocessing is fitted on the development set. Nested cross-validation checks the primary model.

## Treatment effects

- **Average effect:** g-formula, stabilised IPW, marginal structural model and AIPW on the common propensity support, plus a doubly robust estimator with overlap weights. Five-fold cross-fitted LightGBM nuisance models. E-value and a bias-factor grid for unmeasured confounding.
- **Individual effect:** DR-learner (five-fold cross-fitted histogram gradient boosting nuisance models, pseudo-outcome regression), with S-, T- and X-learners as comparators. Benefit `b = -CATE`, so positive values mean treatment is estimated to lower mortality.

## The Prescriptive Safety Audit

Policy at threshold `t`: treat if predicted risk `r >= t`.

$$
\Delta_i(t)=\begin{cases}
b_i & A_i=1,\ r_i<t \quad\text{(support withdrawn)}\\
-b_i & A_i=0,\ r_i\ge t \quad\text{(support escalated)}\\
0 & \text{otherwise}
\end{cases}
$$

A change is harmful when $\Delta_i(t) > \delta$, with $\delta = 0.01$.

| Quantity | Definition | Role |
|---|---|---|
| EED(t) | $1000 \times \sum_i \Delta_i(t) / N$, net expected excess deaths per 1000 patients | **Primary output**, reported at every threshold |
| EED split | Withdrawal and escalation contributions to EED(t) | Shows which decisions drive the estimate |
| HRR(t) | harmful changes / N | Share of the cohort harmed |
| HFR(t) | harmful changes / all changes | Share of changes that harm |
| DHI | mean of EED(t) over 41 thresholds from 0.02 to 0.60 | Secondary, exploratory summary |
| PSS | mean of 1 - HFR(t) over the same thresholds | Secondary, exploratory summary |
| CAR(t) | share of patients where `r >= t` agrees with `b > delta` | Alignment of risk and benefit |
| Rank concordance | P(higher risk also has higher benefit) for random pairs | Below 0.5 means risk and benefit are inversely ranked |
| Treatment Influence Index | mean absolute change in a treatment-aware model's risk when A is toggled | How much treatment shapes predicted risk |

DHI and PSS weight all thresholds equally, depend on the harm margin and are conditional on the benefit estimates. They are not validated safety measures.

## Validity gate (screening checks)

1. **Direction:** the adjusted average effect agrees with clinical knowledge.
2. **Discrimination:** the c-for-benefit exceeds a reference floor from the semi-synthetic benchmark (0.608 for 50% recovery of the true hazard in that benchmark).
3. **Calibration:** predicted benefit tracks observed benefit.

The checks are diagnostic and work in one direction. Failure means the audit verdict is reported as **not verified**. Passing does not certify the verdict: the c-for-benefit measures ranking, not policy value; the contrasts behind checks 2 and 3 are unadjusted or matched only on predicted risk; and the floor is specific to one simulation.

## Semi-synthetic benchmark

12,000 simulated patients per replicate (20 replicates), eight covariates, confounded treatment, known benefit. Benefit estimates are mixed with noise in proportion alpha from 0 to 1 (12 steps). Recovery of the true DHI equals 1 - alpha by construction; the informative output is the c-for-benefit reached at each noise level. Only random noise is examined; offsets, sign errors, miscalibration and overlap failure are not.

## The TRIGGER checklist (proposed)

| | Item | Question |
|---|---|---|
| **T** | Treatment decision | What will the score trigger, for which patients, at which threshold? |
| **R** | Realistic direction | Do adjusted effect estimates agree in direction with clinical knowledge and trial evidence? |
| **I** | Individual benefit | Do benefit estimates rank patients and calibrate well? |
| **G** | Graded consequences | Are consequences reported at every threshold, separately for escalation and withdrawal? |
| **G** | Groups and settings | Are results reported by sex, age and other groups, and in an external cohort? |
| **E** | Equivalent models | Do audit results distinguish between candidate models? |
| **R** | Restraint | If the checks fail, is the verdict reported as not verified and is further evaluation planned? |

TRIGGER is a proposal derived from this work. It has not been validated or endorsed through a consensus process, and passing every item does not certify safety.
