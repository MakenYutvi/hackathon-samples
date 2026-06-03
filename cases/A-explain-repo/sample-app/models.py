"""Domain models for the feature board.

These are plain dataclasses; persistence lives in storage.py.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class User:
    id: int
    name: str
    token: str


@dataclass
class FeatureRequest:
    id: int
    title: str
    description: str
    author_id: int
    effort: int  # t-shirt size 1..5, larger means more work
    created_at: datetime
    voter_ids: List[int] = field(default_factory=list)

    @property
    def vote_count(self) -> int:
        return len(self.voter_ids)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author_id": self.author_id,
            "effort": self.effort,
            "created_at": self.created_at.isoformat(),
            "votes": self.vote_count,
        }
