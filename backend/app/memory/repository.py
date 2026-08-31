"""Persistence boundary for GraveyAI memory."""

from typing import Protocol
from uuid import UUID

from .models import MemoryItem, MemoryScope


class PersistentMemoryRepository(Protocol):
    """Provider-neutral contract for production memory persistence."""

    def save(self, item: MemoryItem) -> MemoryItem: ...

    def get(self, memory_id: UUID, owner_id: str) -> MemoryItem | None: ...

    def list(self, owner_id: str, scope: MemoryScope | None = None) -> list[MemoryItem]: ...

    def delete(self, memory_id: UUID, owner_id: str) -> bool: ...


class PostgresMemoryRepository:
    """Production adapter boundary.

    Database I/O is intentionally not embedded in the domain model. The adapter
    can be implemented with PostgreSQL/pgvector once the application's database
    configuration and migration system are established.
    """

    def __init__(self, database_url: str) -> None:
        if not database_url.strip():
            raise ValueError("database_url is required")
        self.database_url = database_url

    def save(self, item: MemoryItem) -> MemoryItem:
        raise NotImplementedError("PostgreSQL persistence is not implemented yet")

    def get(self, memory_id: UUID, owner_id: str) -> MemoryItem | None:
        raise NotImplementedError("PostgreSQL persistence is not implemented yet")

    def list(self, owner_id: str, scope: MemoryScope | None = None) -> list[MemoryItem]:
        raise NotImplementedError("PostgreSQL persistence is not implemented yet")

    def delete(self, memory_id: UUID, owner_id: str) -> bool:
        raise NotImplementedError("PostgreSQL persistence is not implemented yet")
