# Phase 6B — Identity & Session Security

Phase 6B establishes the security boundary for GraveyAI user identity.

## Goals

- Separate identity from AI/RAG business logic.
- Use opaque, high-entropy session tokens.
- Store token fingerprints rather than raw session tokens when persistence is required.
- Keep authentication provider-agnostic.
- Prepare for OAuth/OIDC and managed identity providers.

## Planned production flow

```text
Browser
  ↓
Secure HTTPS session
  ↓
Authentication provider (OIDC/OAuth)
  ↓
GraveyAI session boundary
  ↓
User identity
  ↓
Chat / RAG / provenance APIs
```

## Security rules

1. Never commit secrets, API keys, passwords, or session tokens.
2. Never store plaintext passwords.
3. Use HTTPS in production.
4. Prefer Secure + HttpOnly + SameSite cookies for browser sessions.
5. Validate authorization on every protected API operation.
6. Keep authentication logs free of credentials and sensitive content.
7. Add CSRF protection where cookie-based state-changing requests require it.
8. Rate-limit authentication endpoints.
9. Add account recovery and MFA through the identity provider rather than inventing custom cryptography.

## Status

The domain models, security primitives, and provider-agnostic service contract are now in place. The next increment will connect these contracts to a real OIDC provider and protected FastAPI routes.
