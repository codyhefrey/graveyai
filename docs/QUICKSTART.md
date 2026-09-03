# GraveyAI Quickstart

## Docker Compose

From the repository root:

```bash
cp .env.example .env
docker compose up --build
```

The API is bound to `127.0.0.1:8000` and PostgreSQL to `127.0.0.1:5432`. Compose waits for PostgreSQL health before starting the API and exposes an API healthcheck.

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

## Backend tests

```bash
cd backend
python -m pip install -r requirements.txt
python -m pytest -q
```

The PostgreSQL integration test runs when `GRAVEYAI_TEST_DATABASE_URL` is configured. CI provides a disposable pgvector PostgreSQL service.

## Frontend

```bash
cd frontend
npm install
npm run dev
```

The current frontend is a presentation shell. API-backed conversation and knowledge controls remain a later integration milestone.

## Security notes

- Never use the development identity provider outside development.
- Replace all local `change-me` credentials before any non-local deployment.
- Keep API keys in environment secrets, never in source control.
- Production identity, authorization, retention enforcement, encryption, observability, and distributed deployment remain release-gated.

## Reproducibility

Run the backend tests and frontend build in CI before promoting a branch into an integration or release branch.
