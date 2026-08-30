# GraveyAI Architecture

## System boundaries

GraveyAI is designed as a modular application with a web client, API layer, AI services, retrieval services, and persistent storage.

### Core flow

1. A client sends a request to the API.
2. The API validates the request and applies authentication/authorization as those capabilities are introduced.
3. The AI service determines whether external knowledge retrieval is required.
4. The retrieval layer searches indexed knowledge and returns relevant context.
5. The model generates a response using the available context.
6. The API returns the response and appropriate metadata to the client.

## Design goals

- Provider-agnostic AI integration
- Evidence-aware responses
- Explicit separation of retrieval and generation
- Secure handling of secrets and user data
- Observable, testable services
- Incremental deployment from local development to cloud infrastructure

## Planned components

- `frontend/` — browser client
- `backend/app/api/` — HTTP/API routes
- `backend/app/ai/` — model adapters and AI orchestration
- `backend/app/rag/` — ingestion, chunking, embeddings, and retrieval
- `backend/app/models/` — application/domain models
- `backend/app/services/` — reusable application services
- PostgreSQL — application persistence
- pgvector — vector similarity search
