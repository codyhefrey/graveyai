import os
from pathlib import Path

import pytest
import psycopg

from app.memory.models import MemoryItem, MemoryScope
from app.memory.postgres import PostgresMemoryRepository


DATABASE_URL = os.getenv("GRAVEYAI_TEST_DATABASE_URL")


@pytest.mark.skipif(not DATABASE_URL, reason="PostgreSQL integration database not configured")
def test_postgres_memory_crud_and_owner_isolation() -> None:
    assert DATABASE_URL is not None
    with psycopg.connect(DATABASE_URL) as connection:
        migrations = Path(__file__).parents[1] / "migrations"
        for migration in sorted(migrations.glob("*.sql")):
            connection.execute(migration.read_text(encoding="utf-8"))
        connection.commit()

        repository = PostgresMemoryRepository(connection)
        item = MemoryItem(
            owner_id="integration-user-1",
            content="research memory",
            scope=MemoryScope.RESEARCH,
            source="integration-test",
        )
        repository.save(item)

        assert repository.get(item.memory_id, "integration-user-1") == item
        assert repository.get(item.memory_id, "integration-user-2") is None
        assert repository.list("integration-user-1", MemoryScope.RESEARCH) == [item]
        with pytest.raises(PermissionError):
            repository.save(
                MemoryItem(
                    owner_id="integration-user-2",
                    memory_id=item.memory_id,
                    content="unauthorized overwrite",
                    scope=MemoryScope.RESEARCH,
                )
            )
        assert repository.get(item.memory_id, "integration-user-1") == item
        assert repository.delete(item.memory_id, "integration-user-2") is False
        assert repository.delete(item.memory_id, "integration-user-1") is True
        assert repository.get(item.memory_id, "integration-user-1") is None
