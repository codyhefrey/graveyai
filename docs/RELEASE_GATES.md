# GraveyAI Release Gates

A capability is not promoted to a stable release solely because its happy path works.

## Gate 1 — Architecture

- Clear responsibility and interface boundary.
- Dependencies documented.
- Failure modes identified.
- Migration and replacement path documented.

## Gate 2 — Correctness

- Unit tests pass.
- Integration/API tests pass.
- Negative paths are tested.
- Data validation is explicit.

## Gate 3 — Security

- Authentication and authorization reviewed.
- Secrets excluded from source control.
- Input/resource limits defined.
- Sensitive data handling documented.
- Abuse and failure scenarios considered.

## Gate 4 — Reliability

- Timeouts and bounded retries where appropriate.
- External dependency failures handled.
- Health/readiness behavior defined.
- Recovery and rollback path documented.

## Gate 5 — Observability

- Structured logging appropriate to the component.
- Metrics for critical operations.
- Audit events for security-sensitive actions.
- No sensitive payloads emitted by default.

## Gate 6 — Evaluation

AI capabilities require measurable evaluation where feasible. Retrieval quality, latency, correctness, safety, and regression behavior should be benchmarked rather than described only through demonstrations.

## Gate 7 — Documentation

- API/interface documented.
- Configuration documented.
- Known limitations documented.
- Release notes prepared.
- Operational guidance available.

## Gate 8 — Release classification

Only after the preceding gates are satisfied should a capability be classified as experimental, alpha, beta, or stable.
