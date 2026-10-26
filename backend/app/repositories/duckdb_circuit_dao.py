from __future__ import annotations
from typing import Optional
from uuid import UUID
import duckdb
from app.domain.circuit_version import CircuitVersion
from app.repositories.interfaces import ICircuitRepository


class DuckDBCircuitDAO(ICircuitRepository):
    def __init__(self):
        self.con = duckdb.connect(database=":memory:")
        self.con.execute(
            "CREATE TABLE IF NOT EXISTS circuit_versions ("
            "version_id VARCHAR PRIMARY KEY, "
            "source_code TEXT, qasm TEXT, version_number INTEGER, depth INTEGER, gate_count INTEGER)"
        )

    def save(self, circuit: CircuitVersion) -> None:
        self.con.execute(
            "INSERT INTO circuit_versions VALUES (?, ?, ?, ?, ?, ?)",
            [
                str(circuit.version_id),
                circuit.source_code,
                circuit.qasm,
                circuit.version_number,
                circuit.metrics.depth if circuit.metrics else 0,
                circuit.metrics.gate_count if circuit.metrics else 0,
            ],
        )

    def find_by_id(self, id: UUID) -> Optional[CircuitVersion]:
        return None  # simplified for MVP

    def find_by_hash(self, hash_value: str) -> Optional[CircuitVersion]:
        return None  # simplified for MVP