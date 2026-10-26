"""Seed script for local development data."""

from app.domain.quantum_job import QuantumJob
from app.domain.circuit_version import CircuitVersion
from app.domain.qiskit_circuit import QiskitCircuit, QuantumGate
from app.domain.refactor_metrics import RefactorMetrics


def seed():
    circuit = QiskitCircuit(qubit_count=2, gates=[QuantumGate("h", [0])])
    metrics = RefactorMetrics(depth=3, gate_count=2, qubit_count=2, fidelity_estimate=0.99, transpiler_level=2)
    version = CircuitVersion(circuit=circuit, source_code="qc = QuantumCircuit(2)", qasm="OPENQASM 2.0;", metrics=metrics)
    print(f"Seeded circuit version: {version.version_id}")

    job = QuantumJob(circuit_version_id=version.version_id, shots=1024, counts={"00": 512, "11": 512}, status="COMPLETED")
    print(f"Seeded quantum job: {job.job_id}")


if __name__ == "__main__":
    seed()