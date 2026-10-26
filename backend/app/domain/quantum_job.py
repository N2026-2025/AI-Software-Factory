from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Dict, Optional, List
from app.domain.job_execution_log import JobExecutionLog


@dataclass
class QuantumJob:
    job_id: UUID = field(default_factory=uuid4)
    circuit_version_id: UUID = None  # type: ignore
    shots: int = 1024
    counts: Dict[str, int] = field(default_factory=dict)
    status: str = "PENDING"
    trace_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    logs: List[JobExecutionLog] = field(default_factory=list)

    def add_log(self, log: JobExecutionLog) -> None:
        self.logs.append(log)

    def transition_to(self, new_status: str) -> None:
        self.status = new_status
        self.add_log(
            JobExecutionLog(
                job_id=self.job_id,
                level="INFO",
                message=f"Transitioned to {new_status}",
            )
        )