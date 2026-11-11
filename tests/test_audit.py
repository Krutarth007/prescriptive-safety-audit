import numpy as np
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from psa import deployment_delta, metrics_at, sweep, summarise, c_for_benefit, screening_checks

rng = np.random.default_rng(0)
N = 5000
r = rng.uniform(0, 1, N)
a = rng.binomial(1, 0.4, N)
b = rng.normal(0, 0.1, N)
y = rng.binomial(1, 0.1, N)


def test_zero_benefit_gives_zero_excess_events():
    res = sweep(r, a, np.zeros(N))
    assert all(abs(x.eed_net) < 1e-12 for x in res)


def test_delta_signs():
    delta, flip, wd, esc = deployment_delta(r, a, b, 0.3)
    assert np.allclose(delta[wd], b[wd]) and np.allclose(delta[esc], -b[esc])
    assert np.all(delta[~flip] == 0)


def test_withdraw_plus_escalate_equals_net():
    for x in sweep(r, a, b):
        assert abs(x.eed_withdraw + x.eed_escalate - x.eed_net) < 1e-9


def test_constant_offset_shifts_audit_but_not_c_for_benefit():
    k, t = 0.05, 0.3
    _, _, wd, esc = deployment_delta(r, a, b, t)
    shift = metrics_at(r, a, b + k, t).eed_net - metrics_at(r, a, b, t).eed_net
    assert abs(shift - 1000 * k * (wd.sum() - esc.sum()) / N) < 1e-9
    assert c_for_benefit(b, y, a, r) == c_for_benefit(b + k, y, a, r)


def test_screening_checks_fail_closed():
    out = screening_checks(ate=+0.06, expected_sign=-1, cfb=0.55, cfb_floor=0.61)
    assert out["verdict"] == "not verified"


def test_summary_keys():
    s = summarise(sweep(r, a, b))
    assert {"DHI", "PSS", "DHI_withdraw", "DHI_escalate"} <= set(s)
