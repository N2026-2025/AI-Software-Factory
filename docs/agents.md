# Agent Team Specification

## Roles and Responsibilities

| Agent | Role | Responsibility |
|-------|------|----------------|
| Orchestrator | Capataz | Decomposes PRD into atomic tasks, assigns priorities |
| Qiskit Refactor Agent | Refactorizador | Modernizes Qiskit legacy code, applies transpiler passes |
| Quantum QA Agent | QA Cuántica | Writes and executes tests for circuits (unitarity, equivalence) |
| Revisor Senior | Revisor | Reviews PR vs requirements, writes documentation and PR summary |
| On-Call Agent | Responder | Wakes on alert, executes runbook, reverts faulty refactor, opens PR |

## Process
1. Orchestrator receives a request and decomposes it into tasks.
2. Tasks are delegated to specialized agents with scoped context.
3. Each agent produces an artifact (circuit, test, report, PR).
4. Revisor Senior approves before merge.
5. On-Call Agent operates in production upon alert.

## Communication
- Agents communicate through the Orchestrator (Indirection pattern).
- MCP server exposes tools: validate_qiskit_circuit, transpile_circuit, run_quantum_job, get_backend_info.