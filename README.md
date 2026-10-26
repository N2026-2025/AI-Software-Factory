# Quantum Data Factory — AI Software Factory for Quantum Data Engineering

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Licencia

Este proyecto está bajo la licencia **Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)**.

© 2026 [Tu Nombre]

## Problem Description

Quantum Data Factory is a full-stack AI-assisted application that refactors legacy Qiskit (Python quantum computing) code, executes quantum jobs on a local deterministic simulator (Qiskit Aer), and persists results in a relational database. It is designed as a single application taken from specification to production, following the ai-dev-tools-zoomcamp final project workflow.

### The problem

Teams working with quantum computing in data engineering face legacy Qiskit code that breaks across Qiskit versions, lacks unit tests, has no observability, and cannot be integrated into classical data pipelines (ETL/ELT). There is no factory that converts quantum legacy code into maintainable, testable, and operable data pipelines.

### What the system does

- Accepts legacy Qiskit Python code via a React UI.
- Refactors the circuit using AI-assisted services (modernizes imports, applies transpiler levels, reports depth and gate count).
- Executes the circuit on Qiskit Aer (free, local, deterministic simulator).
- Persists jobs, circuit versions, metrics, and execution logs in PostgreSQL.
- Exposes a FastAPI backend with OpenAPI documentation.
- Includes an on-call agent skeleton that reacts to job failures.
- Runs locally with a single command: `docker compose up`.

### Expected behavior

- A user uploads a `.py` file with a `QuantumCircuit`.
- The backend validates, refactors, and stores the circuit version.
- The user can submit a quantum job and view counts/histograms.
- All requests carry a `trace_id` propagated to logs and database records.

## Stack

- Backend: FastAPI + SQLAlchemy + Python 3.11
- UI: React 18 + Vite + Tailwind CSS
- Database: PostgreSQL (persistent), DuckDB (ephemeral validation)
- Quantum: Qiskit + Qiskit Aer (local simulator)
- Containerization: Docker + Docker Compose
- CI/CD: GitHub Actions

## Commands

```bash
# Full stack (one command)
docker compose up

# Backend tests
cd backend && pip install -r requirements.txt && pytest

# UI tests
cd frontend && npm install && npm test
```
