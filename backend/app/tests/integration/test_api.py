from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_refactor_endpoint():
    response = client.post(
        "/api/v1/refactor",
        json={"source_code": "from qiskit import QuantumCircuit\nqc = QuantumCircuit(2)\n"},
    )
    assert response.status_code == 200
    body = response.json()
    assert "version_id" in body
    assert "depth" in body