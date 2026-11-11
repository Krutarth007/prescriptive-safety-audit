"""Prescriptive Safety Audit: a small, dependency-light implementation.

The audit asks what would happen to patients if a risk score were used to allocate a binary
treatment with the rule "treat if predicted risk >= t". It needs three arrays per patient:

    r : predicted risk from any model, in [0, 1]
    a : observed treatment (1 = treated, 0 = untreated)
    b : estimated individual benefit of treatment, b = -CATE
        (positive values mean treatment is estimated to lower the risk of the outcome)

For a threshold t, the policy changes care where it disagrees with observed care:

    withdraw  (a = 1, r < t):  change in expected risk  delta =  b
    escalate  (a = 0, r >= t): change in expected risk  delta = -b
    otherwise:                 delta = 0

A change is counted as harmful when delta > margin (default 0.01).

This module mirrors the definitions used in the analysis notebooks (Notebook 2, section 4). It is
provided so that the audit can be reused with any risk model and any binary treatment without
running the full pipeline. The audit is only as good as the benefit estimates b; see
``screening_checks`` and the README for what the outputs do and do not mean.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np

DEFAULT_THRESHOLDS = np.linspace(0.02, 0.60, 41)


def _as_arrays(r, a, b):
    r = np.asarray(r, dtype=float).ravel()
    a = np.asarray(a).astype(int).ravel()
    b = np.asarray(b, dtype=float).ravel()
    if not (len(r) == len(a) == len(b)):
        raise ValueError("r, a and b must have the same length")
    if not set(np.unique(a)).issubset({0, 1}):
        raise ValueError("a must be binary (0/1)")
    return r, a, b


def deployment_delta(r, a, b, t):
    """Per-patient change in expected outcome risk under the policy 'treat if r >= t'.

    Returns (delta, flip, withdraw, escalate) as arrays of length N.
    """
    r, a, b = _as_arrays(r, a, b)
    action = (r >= t).astype(int)
    withdraw = (a == 1) & (action == 0)
    escalate = (a == 0) & (action == 1)
    delta = np.where(withdraw, b, np.where(escalate, -b, 0.0))
    flip = action != a
    return delta, flip, withdraw, escalate


@dataclass
class ThresholdResult:
    threshold: float
    eed_net: float          # net expected excess events per 1000 patients (positive = net harm)
    eed_withdraw: float     # contribution of withdrawals per 1000
    eed_escalate: float     # contribution of escalations per 1000
    eed_harmful: float      # excess events per 1000 from harmful changes only
    hrr: float              # harmful recommendation rate: harmful changes / N
    hfr: float              # harmful flip rate: harmful changes / all changes
    flip_rate: float        # share of patients whose care would change
    n_changes: int
    n_harmful: int
    car: float              # counterfactual agreement rate: (r >= t) agrees with (b > margin)


def metrics_at(r, a, b, t, margin=0.01):
    """All audit metrics at one threshold."""
    r, a, b = _as_arrays(r, a, b)
    n = len(r)
    delta, flip, withdraw, escalate = deployment_delta(r, a, b, t)
    harmful = flip & (delta > margin)
    n_flip = int(flip.sum())
    return ThresholdResult(
        threshold=float(t),
        eed_net=float(delta.sum() / n * 1000),
        eed_withdraw=float(delta[withdraw].sum() / n * 1000),
        eed_escalate=float(delta[escalate].sum() / n * 1000),
        eed_harmful=float(delta[harmful].sum() / n * 1000),
        hrr=float(harmful.mean()),
        hfr=float(harmful.sum() / n_flip) if n_flip > 0 else float("nan"),
        flip_rate=float(flip.mean()),
        n_changes=n_flip,
        n_harmful=int(harmful.sum()),
        car=float(np.mean((r >= t) == (b > margin))),
    )


def sweep(r, a, b, thresholds=DEFAULT_THRESHOLDS, margin=0.01):
    """Audit metrics across thresholds. Returns a list of ThresholdResult (the primary output)."""
    return [metrics_at(r, a, b, t, margin) for t in thresholds]


def summarise(results):
    """Secondary, exploratory summaries over a sweep.

    DHI  : Deployment Hazard Index, mean net excess events per 1000 across thresholds (lower is safer)
    PSS  : Prescriptive Safety Score, mean share of policy-induced changes that are not harmful (1 is safest)
    Both weight every threshold equally and are conditional on the benefit estimates; neither is a
    validated safety measure. Report the threshold-specific curve alongside them.
    """
    eed = np.array([x.eed_net for x in results])
    hfr = np.array([x.hfr for x in results])
    return {
        "DHI": float(eed.mean()),
        "DHI_withdraw": float(np.mean([x.eed_withdraw for x in results])),
        "DHI_escalate": float(np.mean([x.eed_escalate for x in results])),
        "PSS": float(np.nanmean(1 - hfr)),
        "thresholds_with_net_harm": int((eed > 0).sum()),
        "CAR_mean": float(np.nanmean([x.car for x in results])),
    }


def rank_concordance(r, b, n_pairs=20000, seed=0):
    """Probability that, of two random patients, the one at higher risk also has higher estimated benefit.

    Values below 0.5 mean risk and benefit are inversely ranked (benefit-risk inversion).
    """
    r = np.asarray(r, float); b = np.asarray(b, float)
    rng = np.random.default_rng(seed); n = len(r)
    i = rng.integers(0, n, n_pairs); j = rng.integers(0, n, n_pairs)
    ok = (r[i] != r[j]) & (b[i] != b[j])
    return float(((r[i] > r[j]) == (b[i] > b[j]))[ok].mean())


def c_for_benefit(b, y, a, match_score, n_pairs=4000, seed=0):
    """c-for-benefit with treated patients matched to the untreated patient adjacent in match_score.

    Observed pair benefit = untreated outcome - treated outcome; predicted pair benefit = mean of the
    two estimates. 0.5 means no ability to rank patients by benefit. Matching on predicted risk keeps
    the pairs independent of the benefit model, but the contrast is not a causal reference when
    treatment is confounded.
    """
    b = np.asarray(b, float); y = np.asarray(y).astype(int); a = np.asarray(a).astype(int)
    m = np.asarray(match_score, float)
    rng = np.random.default_rng(seed)
    t_idx = np.where(a == 1)[0]; c_idx = np.where(a == 0)[0]
    if len(t_idx) == 0 or len(c_idx) == 0:
        return float("nan")
    order = np.argsort(m[c_idx]); cs = m[c_idx][order]; c_sorted = c_idx[order]
    pos = np.clip(np.searchsorted(cs, m[t_idx]), 0, len(c_sorted) - 1)
    pt, pc = t_idx, c_sorted[pos]
    obs = y[pc] - y[pt]
    prd = 0.5 * (b[pt] + b[pc])
    i = rng.integers(0, len(pt), n_pairs); k = rng.integers(0, len(pt), n_pairs)
    ok = (prd[i] != prd[k]) & (obs[i] != obs[k])
    if ok.sum() == 0:
        return 0.5
    return float(((prd[i] > prd[k]) == (obs[i] > obs[k]))[ok].mean())


def screening_checks(ate, expected_sign, cfb, cfb_floor, calib_error=None, benefit_sd=None, max_calib_ratio=0.5):
    """Validity gate: three diagnostic checks on the benefit model, used in one direction only.

    Failing any check means the audit verdict should be reported as *not verified*.
    Passing all checks does NOT certify the verdict: the c-for-benefit measures ranking, not policy
    value, and the floor is a reference point from a benchmark, not a transferable threshold.

    ate           : adjusted average treatment effect (risk difference)
    expected_sign : sign expected from clinical knowledge (-1 if treatment should lower risk)
    cfb           : c-for-benefit of the benefit estimates
    cfb_floor     : reference floor (for example from a semi-synthetic benchmark)
    calib_error   : mean calibration error for benefit (optional)
    benefit_sd    : spread (SD) of the benefit estimates (optional)
    max_calib_ratio : calibration fails if calib_error >= max_calib_ratio * benefit_sd. The default (0.5)
                    is an illustrative choice, not a validated threshold; set it for your setting.
    """
    checks = {
        "direction": bool(np.sign(ate) == np.sign(expected_sign)),
        "discrimination": bool(cfb >= cfb_floor),
    }
    if calib_error is not None and benefit_sd is not None:
        checks["calibration"] = bool(calib_error < max_calib_ratio * benefit_sd)
    checks["verdict"] = "may be considered (not certified)" if all(checks.values()) else "not verified"
    return checks
