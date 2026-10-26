# GraveYAI — production release gate

**Status:** Backend mock + connected local Next.js development demo, not publicly accessible AI.

## Automatically verifiable
- Python unit tests and frontend compilation.
- Real HTTP: Next.js development POST /api/chat => FastAPI mock /api/v1/chat; invalid messages return 400.
- Next.js production POST /api/chat is **always disabled (503)**, including when an obsolete demo-enable variable is set.
- Python production configuration forbids paid OpenAI calls (503) until authentication, rate limiting, and launch authorization are engineered.

## Blocking launch work
- Proper production identity/token verification, rate limits, abuse handling, auditing, durable conversations and RAG isolation.
- Explicit provider approval, credentials stored securely, privacy protection and integration tests against permitted API endpoints.
- Stable dependency lockfile/version pinning and rollback procedure.
- Authorized hosting, TLS, monitoring, data retention policy, end-to-end browser accessibility/security checks.

**Do not enable a live model on a public unprotected endpoint.**
