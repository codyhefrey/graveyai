"""Policy evaluation for controlled GraveyAI memory retention."""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from .models import MemoryItem, MemoryScope


@dataclass(frozen=True)
class MemoryPolicyDecision:
    allowed: bool
    expires_at: datetime | None
    reason: str


class MemoryPolicy:
    """Small, deterministic policy engine for the Phase 11 foundation.

    This is an application policy boundary, not a substitute for authorization
    middleware or a full privacy/compliance policy system.
    """

    DEFAULT_TTLS = {
        MemoryScope.SESSION: timedelta(hours=24),
        MemoryScope.USER: timedelta(days=365),
        MemoryScope.RESEARCH: timedelta(days=365 * 2),
        MemoryScope.ORGANIZATION: timedelta(days=365),
    }

    def evaluate(self, *, owner_id: str, content: str, scope: MemoryScope) -> MemoryPolicyDecision:
        if not owner_id.strip():
            return MemoryPolicyDecision(False, None, "owner_id is required")
        if not content.strip():
            return MemoryPolicyDecision(False, None, "content is required")
        if len(content) > 100_000:
            return MemoryPolicyDecision(False, None, "memory content exceeds development limit")

        now = datetime.now(timezone.utc)
        return MemoryPolicyDecision(True, now + self.DEFAULT_TTLS[scope], "retention policy accepted")

    def can_read(self, item: MemoryItem, *, owner_id: str) -> bool:
        return item.owner_id == owner_id and not item.is_expired()

    def can_delete(self, item: MemoryItem, *, owner_id: str) -> bool:
        return item.owner_id == owner_id
