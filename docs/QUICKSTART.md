# GraveyAI Quickstart

## Docker Compose

From the repository root:

```bash
cp .env.example .env
docker compose up --build
```

Compose starts PostgreSQL, waits for its health check, applies all SQL migrations, and only then starts the API. The API is bound to `127.0.0.1:8000` and PostgreSQL to `127.0.0.1:5432`.

Verify the API:

```bash
curl http://127.0.0.1:8000/health
```

Development authentication uses the explicit token configured in `.env`:

```bash
curl \
  -H 'Authorization: Bearer development-token' \
  -H 'Content-Type: application/json' \
  -d '{"message":"Hello GraveyAI"}' \
  http://127.0.0.1:8000/api/v1/chat
```

## Memory API

Memory is authenticated and owner-scoped. The current API uses the deterministic in-memory store for development; PostgreSQL persistence is available as a repository adapter and is not silently substituted for the development store.

Create memory:

```bash
curl \
  -H 'Authorization: Bearer development-token' \
  -H 'Content-Type: application/json' \
  -d '{"content":"research note","scope":"research","source":"quickstart"}' \
  http://127.0.0.1:8000/api/v1/memory
```

List memory:

```bash
curl -H 'Authorization: Bearer development-token' \
  http://127.0.0.1:8000/api/v1/memory
```

Individual memory items can be retrieved with `GET /api/v1/memory/{memory_id}` and deleted with `DELETE /api/v1/memory/{memory_id}`. Retention is assigned by the memory policy and expired items are not returned.

## Backend tests

```bash
cd backend
python -m pip install -r requirements.txt
python scripts/migrate.py
python -m pytest -q
```

The PostgreSQL integration test runs when `GRAVEYAI_TEST_DATABASE_URL` is configured. CI provides a disposable pgvector PostgreSQL service.

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The current frontend is a presentation shell. API-backed conversation, memory, and knowledge controls remain a later integration milestone.

## Security notes

- Never use the development identity provider outside development.
- Replace all local `change-me` credentials before any non-local deployment.
- Keep API keys in environment secrets, never in source control.
- Production identity, authorization, retention enforcement, encryption, observability, and distributed deployment remain release-gated.

## Reproducibility

Run migration validation, backend tests, frontend build, Compose validation, and security scanning in CI before promoting a branch into an integration or release branch.
