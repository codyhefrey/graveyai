# Phase 6B — Identity & Session Security

Phase 6B establishes the security boundary for GraveyAI user identity.

## Goals

- Separate identity from AI/RAG business logic.
- Use opaque, high-entropy session tokens in production.
- Store token fingerprints rather than raw session tokens when persistence is required.
- Keep authentication provider-agnostic.
- Prepare for OAuth/OIDC and managed identity providers.

## Implemented development boundary

The current development environment uses an explicit mock identity provider. The mock provider accepts only the configured development token and is disabled outside the development environment. Protected API routes require verified identity rather than merely checking for a syntactically valid `Bearer` header.

## Planned production flow

```text
Browser
  ↓
Secure HTTPS session
  ↓
Authentication provider (OIDC/OAuth)
  ↓
GraveyAI identity verification
  ↓
User identity
  ↓
Authorization policy
  ↓
Chat / RAG / provenance APIs
```

## Security rules

1. Never commit secrets, API keys, passwords, or production session tokens.
2. Never store plaintext passwords.
3. Use HTTPS in production.
4. Prefer Secure + HttpOnly + SameSite cookies for browser sessions where appropriate.
5. Validate authentication and authorization on every protected API operation.
6. Keep authentication logs free of credentials and sensitive content.
7. Add CSRF protection where cookie-based state-changing requests require it.
8. Rate-limit authentication endpoints.
9. Add account recovery and MFA through the identity provider rather than inventing custom cryptography.

## Status

Development authentication is protected and provider-abstracted. Production OIDC verification, authorization policy, session management, MFA/recovery, rate limiting, and deployment-specific security controls remain release-gated work.
