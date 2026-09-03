"""Provider-neutral persistence boundary for GraveyAI memory."""

from typing import Protocol
from uuid import UUID

from .models import MemoryItem, MemoryScope


class PersistentMemoryRepository(Protocol):
    """Contract implemented by development and production memory stores."""

    def save(self, item: MemoryItem) -> MemoryItem: ...

    def get(self, memory_id: UUID, owner_id: str) -> MemoryItem | None: ...

    def list(self, owner_id: str, scope: MemoryScope | None = None) -> list[MemoryItem]: ...

    def delete(self, memory_id: UUID, owner_id: str) -> bool: ...
