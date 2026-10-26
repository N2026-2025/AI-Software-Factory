from app.services.circuit_refactor_service import CircuitRefactorService
from app.repositories.interfaces import ICircuitRepository


class FakeRepo(ICircuitRepository):
    def save(self, circuit): pass
    def find_by_id(self, id): return None
    def find_by_hash(self, hash_value): return None


def test_refactor_service_returns_metrics():
    service = CircuitRefactorService(circuit_repo=FakeRepo())
    version = service.refactor_legacy_code("qc = QuantumCircuit(2)")
    assert version.metrics.depth > 0