from app.domain.qiskit_circuit import QiskitCircuit, QuantumGate
from app.domain.refactor_metrics import RefactorMetrics


def test_circuit_validate_true():
    c = QiskitCircuit(qubit_count=2, gates=[QuantumGate("h", [0])])
    assert c.validate() is True


def test_circuit_transpile_reduces_depth():
    c = QiskitCircuit(qubit_count=2, depth=10)
    t = c.transpile(level=2)
    assert t.depth < c.depth


def test_metrics_defaults():
    m = RefactorMetrics(depth=5, gate_count=3, qubit_count=2, fidelity_estimate=0.99, transpiler_level=2)
    assert m.depth == 5