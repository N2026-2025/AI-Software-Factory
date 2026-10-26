from __future__ import annotations
from typing import Optional, List
from uuid import UUID
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from app.domain.quantum_job import QuantumJob
from app.domain.job_execution_log import JobExecutionLog
from app.repositories.interfaces import IQuantumJobRepository

Base = declarative_base()


class JobORM(Base):
    __tablename__ = "quantum_jobs"
    id = Column(String, primary_key=True)
    circuit_version_id = Column(String, nullable=False)
    shots = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="PENDING")
    trace_id = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    counts = Column(Text, nullable=True)


class PostgresQuantumJobDAO(IQuantumJobRepository):
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, job: QuantumJob) -> None:
        session = self.Session()
        try:
            orm = JobORM(
                id=str(job.job_id),
                circuit_version_id=str(job.circuit_version_id),
                shots=job.shots,
                status=job.status,
                trace_id=job.trace_id,
                created_at=job.created_at,
                counts=str(job.counts),
            )
            session.merge(orm)
            session.commit()
        finally:
            session.close()

    def find_by_id(self, id: UUID) -> Optional[QuantumJob]:
        session = self.Session()
        try:
            orm = session.get(JobORM, str(id))
            if not orm:
                return None
            return QuantumJob(
                job_id=orm.id,
                circuit_version_id=orm.circuit_version_id,
                shots=orm.shots,
                status=orm.status,
                trace_id=orm.trace_id,
                created_at=orm.created_at,
                counts=eval(orm.counts) if orm.counts else {},
            )
        finally:
            session.close()

    def find_by_status(self, status: str) -> List[QuantumJob]:
        session = self.Session()
        try:
            rows = session.query(JobORM).filter_by(status=status).all()
            return [
                QuantumJob(
                    job_id=r.id,
                    circuit_version_id=r.circuit_version_id,
                    shots=r.shots,
                    status=r.status,
                    trace_id=r.trace_id,
                    created_at=r.created_at,
                    counts=eval(r.counts) if r.counts else {},
                )
                for r in rows
            ]
        finally:
            session.close()