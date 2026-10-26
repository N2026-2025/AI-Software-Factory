from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.quantum_job_controller import router as quantum_job_router
from app.observability import setup_trace_middleware

app = FastAPI(title="Quantum Data Factory API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_trace_middleware(app)

app.include_router(quantum_job_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok", "service": "quantum-data-factory"}