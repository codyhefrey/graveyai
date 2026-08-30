from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class User:
    id: str
    email: str
    display_name: str | None = None
    created_at: datetime | None = None


@dataclass(frozen=True)
class Session:
    user_id: str
    session_id: str
    expires_at: datetime
