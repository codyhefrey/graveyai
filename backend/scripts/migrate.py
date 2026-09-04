"""Apply SQL migrations in deterministic filename order."""

import os
from pathlib import Path

import psycopg


MIGRATIONS_DIR = Path(__file__).resolve().parents[1] / "migrations"


def main() -> None:
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL is required")
    # SQLAlchemy URLs are accepted by application configuration, while psycopg
    # expects the underlying PostgreSQL URL scheme.
    database_url = database_url.replace("postgresql+psycopg://", "postgresql://", 1)

    migrations = sorted(MIGRATIONS_DIR.glob("*.sql"))
    if not migrations:
        raise RuntimeError("No SQL migrations found")

    with psycopg.connect(database_url) as connection:
        for migration in migrations:
            connection.execute(migration.read_text(encoding="utf-8"))
        connection.commit()


if __name__ == "__main__":
    main()
