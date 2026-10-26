from __future__ import annotations
from dataclasses import dataclass


@dataclass
class JobResult:
    counts: dict
    status: str
    trace_id: str


class AerSimulatorBackend:
    """Expert: knows how to run a circuit on Qiskit Aer (local, free, deterministic)."""

    def run(self, circuit, shots: int = 1024) -> JobResult:
        # Deterministic mock for MVP; replace with real Qiskit Aer execution
        return JobResult(
            counts={"00": shots // 2, "11": shots // 2},
            status="COMPLETED",
            trace_id="aer-trace",
        )