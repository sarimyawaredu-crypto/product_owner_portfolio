"""How many organizers do we need in an A/B test to detect a change in a conversion rate?

Two sided test of two proportions, normal approximation.
Usage: python tools/sample_size.py --baseline 0.20 --mde 0.05
"""
from __future__ import annotations

import argparse
import math
from statistics import NormalDist


def sample_size_per_group(baseline: float, mde: float, alpha: float = 0.05, power: float = 0.8) -> int:
    """Organizers needed in EACH group to detect an absolute lift of `mde` over `baseline`."""
    if not 0 < baseline < 1 or not 0 < baseline + mde < 1:
        raise ValueError("rates must be between 0 and 1")
    if mde == 0:
        raise ValueError("minimum detectable effect cannot be zero")
    p1, p2 = baseline, baseline + mde
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    num = (z_a * math.sqrt(2 * p_bar * (1 - p_bar)) + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / mde ** 2)


def weeks_needed(per_group: int, weekly_traffic: int, groups: int = 2) -> float:
    return per_group * groups / weekly_traffic


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--baseline", type=float, required=True)
    p.add_argument("--mde", type=float, required=True, help="absolute lift, e.g. 0.05 for 5 points")
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--power", type=float, default=0.8)
    p.add_argument("--weekly", type=int, help="eligible organizers per week")
    a = p.parse_args()
    n = sample_size_per_group(a.baseline, a.mde, a.alpha, a.power)
    print(f"{n} organizers per group ({2 * n} total)")
    if a.weekly:
        print(f"About {weeks_needed(n, a.weekly):.1f} weeks at {a.weekly} organizers per week")
