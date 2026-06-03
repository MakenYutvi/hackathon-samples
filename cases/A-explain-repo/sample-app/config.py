"""Application configuration.

Values are read from the environment with sensible defaults so the app
runs out of the box during the demo.
"""
import os


class Config:
    HOST = os.environ.get("FEATURE_BOARD_HOST", "0.0.0.0")
    PORT = int(os.environ.get("FEATURE_BOARD_PORT", "5000"))
    DEBUG = os.environ.get("FEATURE_BOARD_DEBUG", "true").lower() == "true"

    # Weights used by the priority scoring algorithm.
    VOTE_WEIGHT = 1.0
    RECENCY_WEIGHT = 0.5
    EFFORT_PENALTY = 2.0

    # How many days before a feature's recency bonus fully decays.
    RECENCY_WINDOW_DAYS = 30
