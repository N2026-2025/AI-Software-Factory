from __future__ import annotations
from typing import Optional
from uuid import UUID
from app.domain.quantum_job import QuantumJob
from app.repositories.interfaces import IQuantumJobRepository, ICircuitRepository
from app.infrastructure.aer_backend import AerSimulatorBackend


class QuantumJobService:
    def __init__(
        self,
        job_repo: IQuantumJobRepository,
        circuit_repo: ICircuitRepository,
        backend: AerSimulatorBackend,
    ):
        self.job_repo = job_repo
        self.circuit_repo = circuit_repo
        self.backend = backend

    def submit_job(self, circuit_version_id: UUID, shots: int) -> QuantumJob:
        import uuid
        job = QuantumJob(circuit_version_id=circuit_version_id, shots=shots, trace_id="trace-" + str(uuid.uuid4()))
        self.job_repo.save(job)
        # Simulate execution via expert backend
        result = self.backend.run(circuit=None, shots=shots)
        job.counts = result.counts
        job.transition_to("COMPLETED")
        self.job_repo.save(job)
        return job

    def get_job(self, job_id: UUID) -> Optional[QuantumJob]:
        return self.job_repo.find_by_id(job_id)