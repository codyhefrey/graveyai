"""Apply SQL migrations in deterministic filename order."""

import os
from pathlib import Path

import psycopg


DATABASE_URL = os.environ.get("DATABASE_URL")
MIGRATIONS_DIR = Path(__file__).resolve().parents[1] / "migrations"


def main() -> None:
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL is required")
    migrations = sorted(MIGRATIONS_DIR.glob("*.sql"))
    if not migrations:
        raise RuntimeError("No SQL migrations found")

    with psycopg.connect(DATABASE_URL) as connection:
        for migration in migrations:
            connection.execute(migration.read_text(encoding="utf-8"))
        connection.commit()


if __name__ == "__main__":
    main()
