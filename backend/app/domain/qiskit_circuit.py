from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class QuantumGate:
    name: str
    qubits: List[int]
    params: List[float] = field(default_factory=list)


@dataclass
class QiskitCircuit:
    qubit_count: int
    gates: List[QuantumGate] = field(default_factory=list)
    depth: int = 0

    def validate(self) -> bool:
        """Expert: the circuit knows if it is valid."""
        return self.qubit_count > 0

    def transpile(self, level: int = 1) -> "QiskitCircuit":
        """Expert: the circuit returns a transpiled version of itself."""
        return QiskitCircuit(
            qubit_count=self.qubit_count,
            gates=self.gates,
            depth=max(1, self.depth - level),
        )