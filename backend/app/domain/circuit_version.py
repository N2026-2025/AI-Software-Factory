from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from app.domain.qiskit_circuit import QiskitCircuit
from app.domain.refactor_metrics import RefactorMetrics


@dataclass
class CircuitVersion:
    version_id: UUID = field(default_factory=uuid4)
    circuit: QiskitCircuit = None  # type: ignore
    source_code: str = ""
    qasm: str = ""
    version_number: int = 1
    metrics: RefactorMetrics = None  # type: ignore

    def latest(self) -> "CircuitVersion":
        return self