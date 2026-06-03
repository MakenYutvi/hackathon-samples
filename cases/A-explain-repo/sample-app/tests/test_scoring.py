"""Tests for the priority scoring logic."""
from datetime import datetime, timedelta

from models import FeatureRequest
from scoring import priority, recency_bonus, sort_by_priority


def make_feature(fid, votes, effort, age_days):
    created = datetime.utcnow() - timedelta(days=age_days)
    f = FeatureRequest(
        id=fid,
        title=f"feature {fid}",
        description="",
        author_id=1,
        effort=effort,
        created_at=created,
    )
    f.voter_ids = list(range(votes))
    return f


def test_recency_bonus_decays():
    now = datetime.utcnow()
    fresh = recency_bonus(now, now)
    old = recency_bonus(now - timedelta(days=60), now)
    assert fresh > old
    assert old == 0.0


def test_more_votes_higher_priority():
    a = make_feature(1, votes=10, effort=1, age_days=1)
    b = make_feature(2, votes=2, effort=1, age_days=1)
    assert priority(a) > priority(b)


def test_high_effort_lowers_priority():
    cheap = make_feature(1, votes=5, effort=1, age_days=1)
    pricey = make_feature(2, votes=5, effort=5, age_days=1)
    assert priority(cheap) > priority(pricey)


def test_sort_orders_by_priority():
    features = [
        make_feature(1, votes=1, effort=1, age_days=1),
        make_feature(2, votes=20, effort=1, age_days=1),
        make_feature(3, votes=5, effort=1, age_days=1),
    ]
    ordered = sort_by_priority(features)
    assert [f.id for f in ordered] == [2, 3, 1]
