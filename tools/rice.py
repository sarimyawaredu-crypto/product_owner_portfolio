"""RICE prioritisation for a backlog CSV.

RICE = Reach x Impact x Confidence / Effort
  reach       organizers affected per quarter
  impact      3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal
  confidence  0 to 1, how sure we are about reach and impact
  effort      person weeks

Usage: python tools/rice.py [backlog.csv] [--chart images/rice.png]
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

VALID_IMPACT = {3, 2, 1, 0.5, 0.25}


@dataclass
class Item:
    id: str
    item: str
    epic: str
    reach: float
    impact: float
    confidence: float
    effort: float
    depends_on: tuple[str, ...] = ()

    def __post_init__(self):
        if self.impact not in VALID_IMPACT:
            raise ValueError(f"{self.id}: impact must be one of {sorted(VALID_IMPACT)}")
        if not 0 <= self.confidence <= 1:
            raise ValueError(f"{self.id}: confidence must be between 0 and 1")
        if self.effort <= 0:
            raise ValueError(f"{self.id}: effort must be positive")

    @property
    def score(self) -> float:
        return self.reach * self.impact * self.confidence / self.effort


def load(path: str | Path) -> list[Item]:
    with open(path, newline="", encoding="utf-8") as f:
        return [Item(r["id"], r["item"], r["epic"], float(r["reach"]), float(r["impact"]),
                     float(r["confidence"]), float(r["effort"]),
                     tuple(d for d in (r.get("depends_on") or "").split(";") if d)) for r in csv.DictReader(f)]


def rank(items: list[Item]) -> list[Item]:
    # Ties broken by lower effort: ship the cheaper one first.
    return sorted(items, key=lambda i: (-i.score, i.effort))


def plan_releases(ranked: list[Item], capacity_per_release: float) -> list[list[Item]]:
    """Fill releases in RICE order, but never before an item's dependencies have shipped.

    Pure RICE ranking ignores dependencies: "explain the forecast" can outscore
    the forecast itself. Here an item is only eligible once everything it depends
    on is in the same or an earlier release.
    """
    known = {i.id for i in ranked}
    for it in ranked:
        if it.effort > capacity_per_release:
            raise ValueError(f"{it.id} is larger than a release; split it")
        missing = set(it.depends_on) - known
        if missing:
            raise ValueError(f"{it.id} depends on unknown items {sorted(missing)}")
    remaining = list(ranked)
    scheduled: set[str] = set()
    releases: list[list[Item]] = []
    while remaining:
        release, used = [], 0.0
        progress = True
        while progress:
            progress = False
            for it in remaining:
                ready = all(d in scheduled for d in it.depends_on)
                if ready and used + it.effort <= capacity_per_release:
                    release.append(it)
                    used += it.effort
                    scheduled.add(it.id)
                    remaining.remove(it)
                    progress = True
                    break  # restart in rank order: new items may now be ready
        if not release:
            raise ValueError("Circular dependency in backlog")
        releases.append(release)
    return releases


def to_markdown(ranked: list[Item]) -> str:
    rows = ["| Rank | ID | Item | Reach | Impact | Confidence | Effort | RICE |", "|---|---|---|---|---|---|---|---|"]
    for n, i in enumerate(ranked, 1):
        rows.append(f"| {n} | {i.id} | {i.item} | {i.reach:.0f} | {i.impact:g} | {i.confidence:.0%} | {i.effort:g} | **{i.score:.0f}** |")
    return "\n".join(rows)


def chart(items: list[Item], out: str | Path) -> None:
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5.5))
    for i in items:
        value = i.reach * i.impact * i.confidence
        ax.scatter(i.effort, value, s=60 + i.score * 0.6, alpha=0.75, color="#5b4bdb", edgecolor="white")
        ax.annotate(i.id, (i.effort, value), xytext=(6, 4), textcoords="offset points", fontsize=9)
    ax.set_xlabel("Effort (person weeks)")
    ax.set_ylabel("Value = reach × impact × confidence")
    ax.set_title("Value vs effort: top left is where to start")
    ax.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(out, dpi=130)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("csv", nargs="?", default=Path(__file__).with_name("backlog.csv"))
    p.add_argument("--chart")
    p.add_argument("--capacity", type=float, default=8, help="person weeks per release")
    a = p.parse_args()
    ranked = rank(load(a.csv))
    print(to_markdown(ranked))
    print()
    for n, rel in enumerate(plan_releases(ranked, a.capacity), 1):
        print(f"Release {n}: {', '.join(i.id for i in rel)} ({sum(i.effort for i in rel):g} person weeks)")
    if a.chart:
        chart(ranked, a.chart)
