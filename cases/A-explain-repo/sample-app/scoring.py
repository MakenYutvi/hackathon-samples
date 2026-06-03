"""Priority scoring for feature requests.

priority = votes * VOTE_WEIGHT
         + recency_bonus * RECENCY_WEIGHT
         - effort * EFFORT_PENALTY

recency_bonus decays linearly from 1.0 (just created) to 0.0 once the
feature is older than RECENCY_WINDOW_DAYS.
"""
from datetime import datetime

from config import Config
from models import FeatureRequest


def recency_bonus(created_at: datetime, now: datetime | None = None) -> float:
    now = now or datetime.utcnow()
    age_days = (now - created_at).total_seconds() / 86400.0
    if age_days >= Config.RECENCY_WINDOW_DAYS:
        return 0.0
    return 1.0 - (age_days / Config.RECENCY_WINDOW_DAYS)


def priority(feature: FeatureRequest, now: datetime | None = None) -> float:
    score = feature.vote_count * Config.VOTE_WEIGHT
    score += recency_bonus(feature.created_at, now) * Config.RECENCY_WEIGHT
    score -= feature.effort * Config.EFFORT_PENALTY
    return round(score, 3)


def sort_by_priority(features: list[FeatureRequest], now: datetime | None = None) -> list[FeatureRequest]:
    return sorted(features, key=lambda f: priority(f, now), reverse=True)
