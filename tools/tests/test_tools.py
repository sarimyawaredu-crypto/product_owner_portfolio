import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rice import Item, load, plan_releases, rank  # noqa: E402
from sample_size import sample_size_per_group, weeks_needed  # noqa: E402

CSV = Path(__file__).resolve().parents[1] / "backlog.csv"


def test_rice_score_and_ranking():
    a = Item("A", "a", "e", 100, 2, 0.5, 2)  # 50
    b = Item("B", "b", "e", 100, 1, 1.0, 1)  # 100
    assert a.score == 50 and b.score == 100
    assert [i.id for i in rank([a, b])] == ["B", "A"]


def test_ties_prefer_lower_effort():
    big = Item("BIG", "x", "e", 200, 1, 1, 4)  # 50
    small = Item("SMALL", "x", "e", 100, 1, 1, 2)  # 50
    assert rank([big, small])[0].id == "SMALL"


def test_validation():
    with pytest.raises(ValueError):
        Item("X", "x", "e", 1, 4, 0.5, 1)
    with pytest.raises(ValueError):
        Item("X", "x", "e", 1, 1, 1.5, 1)


def test_release_planning_respects_capacity():
    ranked = rank(load(CSV))
    releases = plan_releases(ranked, 8)
    assert all(sum(i.effort for i in r) <= 8 for r in releases)
    assert sum(len(r) for r in releases) == len(ranked)


def test_sample_size_matches_reference():
    # Reference value for 20% -> 25%, alpha 0.05, power 0.8 is about 1094 per group.
    assert 1080 <= sample_size_per_group(0.20, 0.05) <= 1100
    assert sample_size_per_group(0.20, 0.10) < sample_size_per_group(0.20, 0.05)
    assert weeks_needed(1000, 500) == 4


def test_dependencies_are_respected():
    ranked = rank(load(CSV))
    releases = plan_releases(ranked, 8)
    position = {i.id: n for n, r in enumerate(releases) for i in r}
    for r in releases:
        for i in r:
            for d in i.depends_on:
                assert position[d] <= position[i.id]
    # "Explain the forecast" outranks the forecast on RICE but cannot ship before it
    assert ranked.index(next(i for i in ranked if i.id == "F5")) < ranked.index(next(i for i in ranked if i.id == "F1"))
    assert position["F1"] <= position["F5"]


def test_circular_dependency_detected():
    a = Item("A", "a", "e", 1, 1, 1, 1, ("B",))
    b = Item("B", "b", "e", 1, 1, 1, 1, ("A",))
    with pytest.raises(ValueError):
        plan_releases([a, b], 5)
