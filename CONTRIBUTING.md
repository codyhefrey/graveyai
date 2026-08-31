# Contributing to GraveyAI

Thank you for contributing to GraveyAI.

GraveyAI follows a review-oriented engineering workflow intended for a serious AI research and infrastructure project.

## Branch model

- `main` — stable integration and release-ready code.
- `develop` — active integration branch.
- `feature/*` — focused feature development.
- `phase/*` — major architectural milestones.
- `release/*` — release stabilization.
- `hotfix/*` — urgent fixes to stable releases.

Avoid ad-hoc names such as `final`, `final2`, or `live30`. Branch names should describe purpose and scope.

## Pull requests

Changes should normally flow through a pull request:

```text
Issue / Design
      ↓
feature/* or phase/*
      ↓
Tests + Security Review
      ↓
Pull Request
      ↓
develop
      ↓
release/*
      ↓
main
```

Pull requests should explain the problem, proposed solution, affected components, tests, security considerations, failure behavior, and known limitations.

## Engineering expectations

- Keep modules focused and interfaces explicit.
- Do not commit secrets, credentials, tokens, private keys, or sensitive datasets.
- Add or update tests for behavior changes.
- Preserve provider abstraction boundaries.
- Treat retrieved external content as untrusted input.
- Document breaking API or architectural changes.
- Do not claim a capability is production-ready without satisfying the applicable release gates.

## Research contributions

Research-oriented changes should document assumptions, data sources, evaluation methodology, reproducibility considerations, and limitations where applicable.

## Forks

External contributors may fork the repository and submit pull requests from their fork. Institutional, academic, regional, and experimental deployments should preserve upstream attribution and clearly document deviations from the upstream project.

## Code of conduct

Contributors are expected to communicate professionally, respect other contributors, and focus technical discussion on evidence, reproducibility, security, and engineering quality.
