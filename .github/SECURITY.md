# Security Policy

## Scope

This policy covers security vulnerabilities affecting GraveyAI source code, infrastructure definitions, authentication, authorization, data handling, AI/RAG boundaries, dependencies, and distributed service interfaces.

## Reporting

Please do not disclose exploitable vulnerabilities publicly before a coordinated fix is available. Report security issues privately through the repository's configured GitHub security reporting mechanism when enabled.

Include:

- affected component;
- vulnerability description;
- reproduction steps or proof of concept;
- impact assessment;
- affected versions or commits;
- suggested mitigation, if known.

Do not include real credentials, private keys, personal data, or sensitive production datasets in a report.

## Security principles

GraveyAI follows defense-in-depth principles including least privilege, explicit authentication and authorization, secure secret handling, dependency hygiene, input validation, auditability, and failure isolation.

AI-generated output and retrieved external content are treated as untrusted data and must not automatically receive privileged authority.

## Disclosure

Security fixes should be documented through an appropriate advisory or release note after mitigation is available. Severity and disclosure timing should consider exploitability, affected scope, user impact, and remediation readiness.
