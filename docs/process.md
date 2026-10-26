# Process Documentation

## Development Workflow (SDD + TDD)

1. Write/update `product-spec.md` with user stories and acceptance criteria.
2. Update `openapi.yaml` contract if endpoints change.
3. Write failing tests (unit + integration).
4. Implement domain, repositories (DAO), services, controllers.
5. Run `pytest` and UI tests until green.
6. Refactor applying GRASP patterns.
7. Commit (pre-commit guardrail runs tests and secret scan).

## CI/CD
- GitHub Actions runs tests on every PR.
- Docker images built and pushed on merge to main/develop.
- Deploy to dev is automatic; deploy to production is manual.