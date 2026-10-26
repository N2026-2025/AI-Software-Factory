from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class JobExecutionLog:
    log_id: UUID = field(default_factory=uuid4)  # type: ignore
    job_id: UUID = None  # type: ignore
    timestamp: datetime = field(default_factory=datetime.utcnow)
    level: str = "INFO"
    message: str = ""