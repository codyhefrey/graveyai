# Security and Architecture Baseline

## Ownership and boundaries
This repository is an independent project. Do not copy proprietary code, credentials, customer data, or internal infrastructure details into other repositories or public editions. External integrations must use scoped APIs and explicit authorization.

## Required deployment gates
- [ ] Inventory environments, data classifications, owners, and exposed endpoints.
- [ ] Verify no secret keys or tokens are present in tracked files, history, logs, build artifacts, or browser bundles. Treat suspected exposure as compromised; rotate at the provider and investigate usage.
- [ ] Confirm authentication and object-level, tenant-level authorization on every protected route. Test cross-tenant access denial.
- [ ] Apply per-identity and per-IP rate limits, resource quotas, request-size limits, and provider spending alerts where applicable.
- [ ] Verify encryption in transit, safe secret storage, least-privilege runtime credentials, and access audit trails.
- [ ] Run dependency, secret, and static analysis scans; review and fix actionable findings.
- [ ] Run unit, integration, security, and negative-path tests before release.
- [ ] Check backup restoration, rollback, incident response, and production monitoring.
- [ ] Obtain explicit founder approval for publication, deployment, external submission, or disclosure of proprietary assets.

## Suggested layout (adapt to existing stack)
- `.github/workflows/`: CI and security checks with minimal token permissions.
- `src/` or existing application directories: production code.
- `tests/`: unit, integration, authorization, and abuse tests.
- `docs/`: architecture, threat model, release runbook, incident response.
- `scripts/`: safe, documented developer automation.
- `.env.example`: placeholder names only; never real credentials.

Do not move or rename working entrypoints merely to match this layout. Make structural moves in isolated PRs with passing tests and deployment checks.

## PR security review
Describe threat-model impact, user-visible behavior, migrations, rollback, tests, dependency changes, new permissions, and whether secrets or sensitive data may be involved. Never paste live secrets into issues or PRs.

## Incident handling
If a credential leak or active compromise is suspected: restrict affected access, rotate and revoke credentials, inspect provider audit/billing logs, preserve relevant evidence securely, and follow the incident response process. Deleting a Git commit alone does not revoke a leaked secret.

## Status
This document defines a target baseline, **not** a certification that any control is already deployed or validated.
