# Skill: refactor-qiskit-circuit

Reusable workflow for refactoring legacy Qiskit Python circuits.

## Input
- `source_code`: string containing legacy Qiskit Python code

## Output
- `version_id`: UUID of the stored circuit version
- `depth`: circuit depth after transpilation
- `gate_count`: number of gates
- `qubit_count`: number of qubits

## Steps
1. UI submits code to Controller `/api/v1/refactor`
2. Controller delegates to `CircuitRefactorService`
3. Service validates via `QiskitCircuit.validate()` (Expert)
4. Service transpiles via `QiskitCircuit.transpile()` (Expert)
5. Service computes `RefactorMetrics`
6. `DuckDBCircuitDAO` persists the `CircuitVersion`
7. Controller returns JSON to UI

## Guardrail
- Circuit must validate before transpilation.
- No real QPU token required; uses local Aer simulator.