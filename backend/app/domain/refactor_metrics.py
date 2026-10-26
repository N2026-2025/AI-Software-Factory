from __future__ import annotations
from dataclasses import dataclass


@dataclass
class RefactorMetrics:
    depth: int
    gate_count: int
    qubit_count: int
    fidelity_estimate: float
    transpiler_level: int