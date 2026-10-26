from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from uuid import UUID
from app.services.circuit_refactor_service import CircuitRefactorService
from app.services.quantum_job_service import QuantumJobService

router = APIRouter()


class RefactorRequest(BaseModel):
    source_code: str


class RefactorResponse(BaseModel):
    version_id: str
    depth: int
    gate_count: int
    qubit_count: int


class JobRequest(BaseModel):
    circuit_version_id: str
    shots: int = 1024


class JobResponse(BaseModel):
    job_id: str
    status: str
    trace_id: str


# These would be injected via dependency injection in production
# For MVP, we instantiate here (to be refactored to DI)
def get_refactor_service() -> CircuitRefactorService:
    try:
        from app.repositories.duckdb_circuit_dao import DuckDBCircuitDAO
        repo = DuckDBCircuitDAO()
    except (ModuleNotFoundError, ImportError):
        # Fallback para entornos sin compilador C++ (Windows + Python 3.14)
        from app.repositories.interfaces import ICircuitRepository

        class _FakeRepo(ICircuitRepository):
            def save(self, circuit): pass
            def find_by_id(self, id): return None
            def find_by_hash(self, hash_value): return None
        repo = _FakeRepo()
    return CircuitRefactorService(circuit_repo=repo)


def get_job_service() -> QuantumJobService:
    from app.repositories.postgres_job_dao import PostgresQuantumJobDAO
    from app.infrastructure.aer_backend import AerSimulatorBackend
    from app.repositories.duckdb_circuit_dao import DuckDBCircuitDAO
    job_repo = PostgresQuantumJobDAO(database_url="postgresql+psycopg://qfactory:qfactory@localhost:5432/quantum_factory")
    circuit_repo = DuckDBCircuitDAO()
    backend = AerSimulatorBackend()
    return QuantumJobService(job_repo=job_repo, circuit_repo=circuit_repo, backend=backend)


@router.post("/refactor", response_model=RefactorResponse)
def refactor(req: RefactorRequest, request: Request):
    trace_id = request.state.trace_id
    service = get_refactor_service()
    try:
        version = service.refactor_legacy_code(req.source_code)
        return RefactorResponse(
            version_id=str(version.version_id),
            depth=version.metrics.depth,
            gate_count=version.metrics.gate_count,
            qubit_count=version.metrics.qubit_count,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/quantum-job", response_model=JobResponse)
def run_job(req: JobRequest, request: Request):
    trace_id = request.state.trace_id
    service = get_job_service()
    job = service.submit_job(circuit_version_id=UUID(req.circuit_version_id), shots=req.shots)
    return JobResponse(
        job_id=str(job.job_id),
        status=job.status,
        trace_id=job.trace_id,
    )


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: UUID, request: Request):
    service = get_job_service()
    job = service.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return JobResponse(
        job_id=str(job.job_id),
        status=job.status,
        trace_id=job.trace_id,
    )