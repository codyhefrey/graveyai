"""PostgreSQL persistence adapter for GraveyAI memory."""

from typing import Any
from uuid import UUID

from psycopg.types.json import Jsonb

from .models import MemoryItem, MemoryScope
from .repository import PersistentMemoryRepository


CREATE_MEMORY_ITEMS_SQL = """
CREATE TABLE IF NOT EXISTS memory_items (
    memory_id UUID PRIMARY KEY,
    owner_id TEXT NOT NULL,
    content TEXT NOT NULL,
    scope TEXT NOT NULL CHECK (scope IN ('session', 'user', 'research', 'organization')),
    source TEXT,
    created_at TIMESTAMPTZ NOT NULL,
    expires_at TIMESTAMPTZ,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE INDEX IF NOT EXISTS idx_memory_owner_scope
    ON memory_items (owner_id, scope);

CREATE INDEX IF NOT EXISTS idx_memory_expiry
    ON memory_items (expires_at);
"""


class PostgresMemoryRepository(PersistentMemoryRepository):
    """Concrete repository using an existing psycopg connection."""

    def __init__(self, connection: Any) -> None:
        if connection is None:
            raise ValueError("connection is required")
        self.connection = connection

    def initialize_schema(self) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(CREATE_MEMORY_ITEMS_SQL)
        self.connection.commit()

    def save(self, item: MemoryItem) -> MemoryItem:
        sql = """
        INSERT INTO memory_items
            (memory_id, owner_id, content, scope, source, created_at, expires_at, metadata)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (memory_id) DO UPDATE SET
            content = EXCLUDED.content,
            source = EXCLUDED.source,
            expires_at = EXCLUDED.expires_at,
            metadata = EXCLUDED.metadata
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    str(item.memory_id), item.owner_id, item.content, item.scope.value,
                    item.source, item.created_at, item.expires_at, Jsonb(item.metadata),
                ),
            )
        self.connection.commit()
        return item

    def delete(self, memory_id: UUID, owner_id: str) -> bool:
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM memory_items WHERE memory_id = %s AND owner_id = %s",
                (str(memory_id), owner_id),
            )
            deleted = cursor.rowcount > 0
        self.connection.commit()
        return deleted

    @staticmethod
    def _row_to_item(row: tuple[Any, ...]) -> MemoryItem:
        return MemoryItem(
            memory_id=row[0], owner_id=row[1], content=row[2],
            scope=MemoryScope(row[3]), source=row[4], created_at=row[5],
            expires_at=row[6], metadata=row[7] or {},
        )

    def get(self, memory_id: UUID, owner_id: str) -> MemoryItem | None:
        sql = """
        SELECT memory_id, owner_id, content, scope, source, created_at, expires_at, metadata
        FROM memory_items
        WHERE memory_id = %s AND owner_id = %s
          AND (expires_at IS NULL OR expires_at > CURRENT_TIMESTAMP)
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (str(memory_id), owner_id))
            row = cursor.fetchone()
        return self._row_to_item(row) if row else None

    def list(self, owner_id: str, scope: MemoryScope | None = None) -> list[MemoryItem]:
        sql = """
        SELECT memory_id, owner_id, content, scope, source, created_at, expires_at, metadata
        FROM memory_items
        WHERE owner_id = %s
          AND (expires_at IS NULL OR expires_at > CURRENT_TIMESTAMP)
        """
        params: tuple[Any, ...] = (owner_id,)
        if scope is not None:
            sql += " AND scope = %s"
            params = (owner_id, scope.value)
        sql += " ORDER BY created_at DESC"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            rows = cursor.fetchall()
        return [self._row_to_item(row) for row in rows]
