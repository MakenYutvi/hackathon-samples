"""In-memory storage for users and feature requests.

NOTE: everything lives in process memory and is lost on restart. This is
fine for a demo but is the main reason this service is not production-ready.
"""
import secrets
from datetime import datetime
from typing import Dict, List, Optional

from models import FeatureRequest, User


class Storage:
    def __init__(self) -> None:
        self._users: Dict[int, User] = {}
        self._features: Dict[int, FeatureRequest] = {}
        self._tokens: Dict[str, int] = {}  # token -> user_id
        self._next_user_id = 1
        self._next_feature_id = 1

    # --- users ---

    def create_user(self, name: str) -> User:
        token = secrets.token_hex(16)
        user = User(id=self._next_user_id, name=name, token=token)
        self._users[user.id] = user
        self._tokens[token] = user.id
        self._next_user_id += 1
        return user

    def user_by_token(self, token: str) -> Optional[User]:
        user_id = self._tokens.get(token)
        if user_id is None:
            return None
        return self._users.get(user_id)

    # --- features ---

    def create_feature(self, title: str, description: str, author_id: int, effort: int) -> FeatureRequest:
        feature = FeatureRequest(
            id=self._next_feature_id,
            title=title,
            description=description,
            author_id=author_id,
            effort=effort,
            created_at=datetime.utcnow(),
        )
        self._features[feature.id] = feature
        self._next_feature_id += 1
        return feature

    def get_feature(self, feature_id: int) -> Optional[FeatureRequest]:
        return self._features.get(feature_id)

    def list_features(self) -> List[FeatureRequest]:
        return list(self._features.values())

    def add_vote(self, feature_id: int, user_id: int) -> bool:
        feature = self._features.get(feature_id)
        if feature is None:
            return False
        if user_id not in feature.voter_ids:
            feature.voter_ids.append(user_id)
        return True


# A single shared instance used across the app.
db = Storage()
