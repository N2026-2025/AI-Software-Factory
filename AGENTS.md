# AGENTS.md — Quantum Data Factory

## Stack

- Backend: FastAPI + SQLAlchemy + Python 3.11
- UI: React 18 + Vite + Tailwind CSS
- Database: PostgreSQL (persistent), DuckDB (ephemeral validation)
- Quantum: Qiskit + Qiskit Aer (local simulator)
- Containerization: Docker + Docker Compose
- CI/CD: GitHub Actions

## Rules for AI agents

1. **Spec first:** Any endpoint change goes in `openapi.yaml` (contract), then backend, then UI.
2. **Repository DAO pattern:** All data access goes through `backend/app/repositories/`. No raw SQL in controllers or services.
3. **Domain isolation:** Domain objects in `backend/app/domain/` do not import infrastructure or FastAPI.
4. **Traceability:** Every HTTP request must generate a `trace_id` included in logs and DB records.
5. **Security:** Never commit real tokens. Use `.env.example` only. `IBM_QUANTUM_TOKEN` and `OPENROUTER_API_KEY` must be environment variables.
6. **Tests:** All new logic requires unit tests in `backend/tests/unit/` and integration tests in `backend/tests/integration/`.

## Commands

```bash
# Backend
cd backend && pip install -r requirements.txt
cd backend && uvicorn app.main:app --reload --port 8000

# UI
cd frontend && npm install
cd frontend && npm run dev

# Tests
pytest                      # backend tests (from repo root)
cd frontend && npm test     # UI tests

# Full stack
docker compose up           # one command to start everything
```
