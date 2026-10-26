from __future__ import annotations
from typing import Optional, List
from uuid import UUID
from app.domain.circuit_version import CircuitVersion
from app.domain.quantum_job import QuantumJob


class ICircuitRepository:
    def save(self, circuit: CircuitVersion) -> None:
        raise NotImplementedError

    def find_by_id(self, id: UUID) -> Optional[CircuitVersion]:
        raise NotImplementedError

    def find_by_hash(self, hash_value: str) -> Optional[CircuitVersion]:
        raise NotImplementedError


class IQuantumJobRepository:
    def save(self, job: QuantumJob) -> None:
        raise NotImplementedError

    def find_by_id(self, id: UUID) -> Optional[QuantumJob]:
        raise NotImplementedError

    def find_by_status(self, status: str) -> List[QuantumJob]:
        raise NotImplementedError