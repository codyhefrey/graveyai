import pytest

from app.memory.postgres import PostgresMemoryRepository


def test_postgres_repository_requires_connection():
    with pytest.raises(ValueError, match="connection is required"):
        PostgresMemoryRepository(None)
