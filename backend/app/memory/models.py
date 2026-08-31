"""Domain models for controlled GraveyAI memory."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class MemoryScope(str, Enum):
    SESSION = "session"
    USER = "user"
    RESEARCH = "research"
    ORGANIZATION = "organization"


@dataclass(frozen=True)
class MemoryItem:
    """A retained context item with explicit ownership and lifecycle metadata."""

    owner_id: str
    content: str
    scope: MemoryScope
    memory_id: UUID = field(default_factory=uuid4)
    source: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime | None = None
    metadata: dict[str, str] = field(default_factory=dict)

    def is_expired(self, now: datetime | None = None) -> bool:
        now = now or datetime.now(timezone.utc)
        return self.expires_at is not None and self.expires_at <= now
