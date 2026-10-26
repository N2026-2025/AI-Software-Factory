# AI Systems Design Checklist (FURPS+ + GRASP)

## FURPS+

| Category | Requirement | Status |
|----------|-------------|--------|
| Functionality | Refactor legacy Qiskit circuit | Done |
| Functionality | Execute quantum job on Aer simulator | Done |
| Usability | React UI dashboard for jobs | Done |
| Usability | OpenAPI docs at /docs | Done |
| Reliability | Job failure does not crash system | Done |
| Reliability | Deterministic Aer results | Done |
| Performance | Refactor < 2s for < 50 qubits | Pending |
| Performance | Health endpoint < 200ms | Done |
| Supportability | Structured logs with trace_id | Done |
| Supportability | Tokens in env vars only | Done |

## GRASP

| Pattern | Class / Component | Role |
|---------|-------------------|------|
| Controller | QuantumJobController | Receives HTTP, delegates to services |
| Expert | QiskitCircuit | Knows validate() and transpile() |
| Creator | CircuitRefactorService | Creates CircuitVersion |
| Low Coupling | Services depend on repository interfaces | Done |
| High Cohesion | RefactorMetrics holds only metrics | Done |
| Polymorphism | AerSimulatorBackend implements IQuantumBackend | Done |
| Pure Fabrication | PostgresQuantumJobDAO, DuckDBCircuitDAO | Persistence without domain pollution |
| Indirection | AgentOrchestrator (future) | Decouples agents |
| Protected Variations | CircuitVersion isolates Qiskit version changes | Done |

## Repository DAO

| Interface | Implementation |
|-----------|---------------|
| ICircuitRepository | DuckDBCircuitDAO |
| IQuantumJobRepository | PostgresQuantumJobDAO |
