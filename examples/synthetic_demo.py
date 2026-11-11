"""Run the Prescriptive Safety Audit on simulated data (no clinical data needed).

    python examples/synthetic_demo.py

The simulation follows the semi-synthetic benchmark used in the study: treatment is confounded by
severity, true individual benefit is known, and the risk score is the untreated baseline risk.
We audit the policy 'treat if risk >= t' twice: with the true benefit, and with noisy estimates.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from psa import sweep, summarise, rank_concordance, c_for_benefit


def simulate(n=12000, seed=1):
    rng = np.random.default_rng(seed)
    L = rng.normal(size=(n, 8))
    sev = L[:, 0] + 0.5 * L[:, 1]
    true_benefit = 4 * np.clip(0.18 - 0.11 * sev + 0.17 * L[:, 2] - 0.13 * L[:, 3] + 0.09 * L[:, 4], -0.2, 0.8)
    a = rng.binomial(1, 1 / (1 + np.exp(-(1.4 * sev + 1.8 * (L[:, 2] + L[:, 3])))))
    base = 1 / (1 + np.exp(-(0.8 * sev - 1.2)))
    p = np.clip(base - true_benefit * a, 1e-4, 1 - 1e-4)
    y = rng.binomial(1, p)
    return base, a, y, true_benefit


def main():
    r, a, y, b_true = simulate()
    rng = np.random.default_rng(7)
    noise = rng.normal(0, b_true.std(), len(b_true))
    thresholds = np.quantile(r, np.linspace(0.5, 0.9, 41))
    for label, alpha in [("true benefit", 0.0), ("half noise", 0.5), ("pure noise", 1.0)]:
        b = (1 - alpha) * b_true + alpha * noise
        res = sweep(r, a, b, thresholds)
        s = summarise(res)
        print(f"{label:>12}: DHI {s['DHI']:7.1f} per 1000 | withdraw {s['DHI_withdraw']:7.1f} | "
              f"escalate {s['DHI_escalate']:6.1f} | PSS {s['PSS']:.3f} | "
              f"c-for-benefit {c_for_benefit(b, y, a, r):.3f} | risk-benefit concordance {rank_concordance(r, b):.3f}")
    print("\nThe audit attenuates towards zero as benefit estimates degrade, while the c-for-benefit moves "
          "only modestly.\nA flat or reversed verdict can therefore reflect the benefit model, not the policy.")


if __name__ == "__main__":
    main()
