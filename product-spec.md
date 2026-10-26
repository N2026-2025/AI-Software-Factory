# Product Specification — Quantum Data Factory

## User Stories

### US-1 — Refactor legacy Qiskit circuit

As a data engineer, I want to upload a legacy Qiskit Python script so that the factory refactors it into a modern, transpiled circuit with quality metrics.

Acceptance criteria:

- The API accepts a `.py` source code string.
- The system validates that the code parses as a valid Qiskit circuit.
- The system returns `circuit_version_id`, `depth`, `gate_count`, and `qubit_count`.
- The refactored circuit is stored in the database.

### US-2 — Execute quantum job on local simulator

As a user, I want to run a refactored circuit on Qiskit Aer so that I get deterministic counts without paying for a real QPU.

Acceptance criteria:

- The API accepts `circuit_version_id` and `shots`.
- The job receives a unique `job_id` and `trace_id`.
- The job status transitions: PENDING → RUNNING → COMPLETED/FAILED.
- Results (counts) are stored and retrievable.

### US-3 — View job history and dashboard

As a user, I want to see a list of executed quantum jobs and their status in the UI.

Acceptance criteria:

- The UI lists jobs with status, trace ID, and creation time.
- Clicking a job shows counts and metrics.

## Non-goals

- Real IBM Quantum QPU execution (optional future extension).
- User authentication/authorization.
- Multi-tenant isolation.

## Public task tracker

GitHub Issues / GitHub Projects board linked from this repository. Agents used the tracker to decompose tasks (evidence in commit messages and PR descriptions).
