# GraveyAI

> An AI-powered knowledge and assistance platform built for trustworthy retrieval, multilingual interaction, voice capabilities, and practical everyday assistance.

## Vision

GraveyAI aims to make useful AI accessible through a single platform that can understand questions, retrieve trusted knowledge, work with documents, and eventually communicate through text and voice.

## Current milestone

**Phase 8 — Provenance-aware RAG foundation** is now implemented. GraveyAI can ingest documents through the existing RAG pipeline, preserve SHA3-256 provenance metadata associated with GraveyChain, and expose authenticated retrieval endpoints. The development retriever is intentionally dependency-free so it can later be replaced by PostgreSQL/pgvector without changing the API contract.

### Phase 8 endpoints

- `POST /api/v1/rag/documents` — authenticated document ingestion.
- `POST /api/v1/rag/search` — authenticated knowledge retrieval.

RAG provenance records retain the document hash, SHA3-256 algorithm, GraveyChain association, and quantum-ready metadata.

## Planned capabilities

- AI conversational assistant
- Retrieval-Augmented Generation (RAG)
- Document ingestion and knowledge retrieval
- Multilingual interaction
- Voice input and output
- Authentication and user accounts
- Conversation history and memory
- AI safety and evaluation tooling
- Docker-based local development
- Automated testing and CI/CD

## Architecture

```text
                         ┌──────────────────┐
                         │     GraveyAI     │
                         │   AI Assistant   │
                         └────────┬─────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              ┌──────────┐  ┌──────────┐  ┌───────────┐
              │   Chat   │  │   Voice  │  │ Documents │
              └────┬─────┘  └────┬─────┘  └─────┬─────┘
                   └─────────────┼───────────────┘
                                 ▼
                         ┌───────────────┐
                         │   RAG Layer   │
                         │ Retrieval +   │
                         │ Provenance    │
                         └───────┬───────┘
                                 │
                         ┌───────▼───────┐
                         │   AI Engine   │
                         │ Provider API  │
                         └───────────────┘

             Document → Chunk → SHA3-256 → GraveyChain
```

## Technology direction

- **Frontend:** Next.js + TypeScript
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **Vector search:** pgvector
- **AI:** provider-agnostic interface + OpenAI Responses API adapter
- **Infrastructure:** Docker
- **Testing:** Pytest + API tests
- **CI:** GitHub Actions

## Repository structure

```text
graveyai/
├── .github/workflows/
├── backend/
│   ├── app/
│   │   ├── api/v1/
│   │   ├── ai/
│   │   ├── auth/
│   │   ├── core/
│   │   ├── rag/
│   │   └── voice/
│   └── tests/
├── docs/
├── frontend/
└── docker-compose.yml
```
