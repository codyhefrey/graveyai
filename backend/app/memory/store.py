"""Storage contract and deterministic development implementation."""

from typing import Protocol
from uuid import UUID

from .models import MemoryItem, MemoryScope


class MemoryStore(Protocol):
    def save(self, item: MemoryItem) -> MemoryItem: ...

    def get(self, memory_id: UUID, owner_id: str) -> MemoryItem | None: ...

    def list(self, owner_id: str, scope: MemoryScope | None = None) -> list[MemoryItem]: ...

    def delete(self, memory_id: UUID, owner_id: str) -> bool: ...


class InMemoryMemoryStore:
    """Development store; deliberately not a production persistence backend."""

    def __init__(self) -> None:
        self._items: dict[UUID, MemoryItem] = {}

    def save(self, item: MemoryItem) -> MemoryItem:
        self._items[item.memory_id] = item
        return item

    def get(self, memory_id: UUID, owner_id: str) -> MemoryItem | None:
        item = self._items.get(memory_id)
        if item is None or item.owner_id != owner_id or item.is_expired():
            return None
        return item

    def list(self, owner_id: str, scope: MemoryScope | None = None) -> list[MemoryItem]:
        return [
            item
            for item in self._items.values()
            if item.owner_id == owner_id
            and not item.is_expired()
            and (scope is None or item.scope == scope)
        ]

    def delete(self, memory_id: UUID, owner_id: str) -> bool:
        item = self._items.get(memory_id)
        if item is None or item.owner_id != owner_id:
            return False
        del self._items[memory_id]
        return True
