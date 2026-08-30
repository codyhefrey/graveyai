# GraveyAI

> An AI-powered knowledge and assistance platform built for trustworthy retrieval, multilingual interaction, voice capabilities, and practical everyday assistance.

## Vision

GraveyAI aims to make useful AI accessible through a single platform that can understand questions, retrieve trusted knowledge, work with documents, and eventually communicate through text and voice.

## Current milestone

**Phase 3 — Production AI provider** is now implemented. GraveyAI keeps a provider-agnostic AI interface while adding an OpenAI adapter based on the Responses API. The deterministic mock provider remains the default for tests and local development.

### AI provider modes

- `mock` — deterministic local provider; safe for tests and development.
- `openai` — production provider using `OPENAI_API_KEY` and the configured model.

OpenAI's current model catalog supports the Responses API and client SDKs; GraveyAI keeps the model name configurable so the deployment can evolve without changing application code.

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
                         │   AI Engine   │
                         │ Provider API  │
                         └───────┬───────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
              ┌──────────┐ ┌──────────┐ ┌────────────┐
              │ OpenAI   │ │  Mock    │ │ Future AI  │
              │ Provider │ │ Provider │ │ Providers  │
              └──────────┘ └──────────┘ └────────────┘
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
│   │   ├── core/
│   │   ├── rag/
│   │   ├── models/
│   │   └── services/
│   └── tests/
├── frontend/
├── docs/
├── infrastructure/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## API

### Health

`GET /health`

Returns service status and API version.

### Chat

`POST /api/v1/chat`

Example request:

```json
{
  "message": "Explain artificial intelligence in simple terms."
}
```

The endpoint uses the configured provider. `mock` is the default. To enable the OpenAI provider, configure `AI_PROVIDER=openai` and `OPENAI_API_KEY` in the runtime environment. Never commit API keys to GitHub.

## Roadmap

- [x] Phase 1: Project foundation
- [x] Phase 2: FastAPI backend foundation
- [x] Phase 3: Production AI chat provider
- [ ] Phase 4: RAG and document intelligence
- [ ] Phase 5: Web interface
- [ ] Phase 6: Authentication and user management
- [ ] Phase 7: Voice interface
- [ ] Phase 8: Evaluation, testing, and security hardening
- [ ] Phase 9: Cloud deployment
- [ ] Phase 10: Production readiness

## Development principles

1. Privacy and security by design.
2. Clear separation between application logic and AI providers.
3. Ground answers in retrieved evidence whenever possible.
4. Test critical behavior before adding complexity.
5. Keep the project modular so components can evolve independently.

## Status

**Early development — Phase 3.**

GraveyAI is an evolving open-source project. APIs, architecture, and implementation details may change as the system matures.
