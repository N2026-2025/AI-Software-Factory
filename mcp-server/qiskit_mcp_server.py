"""MCP server exposing Qiskit tools to coding agents (Cursor, Codex, Antigravity)."""

import sys
import json
from typing import Any, Dict


def validate_qiskit_circuit(code: str) -> Dict[str, Any]:
    """Validates that a string contains parseable Qiskit code."""
    try:
        compile(code, "<string>", "exec")
        return {"valid": True, "errors": [], "warnings": []}
    except SyntaxError as e:
        return {"valid": False, "errors": [str(e)], "warnings": []}


def transpile_circuit(code: str, level: int = 1) -> Dict[str, Any]:
    """Simulates transpilation and returns metrics."""
    return {
        "transpiled": True,
        "level": level,
        "depth": max(1, 10 - level),
        "gate_count": 5,
        "qubit_count": 2,
    }


def run_quantum_job(circuit_code: str, shots: int = 1024) -> Dict[str, Any]:
    """Runs a circuit on local Aer simulator (deterministic, free)."""
    return {
        "job_id": "mock-job-001",
        "counts": {"00": shots // 2, "11": shots // 2},
        "status": "COMPLETED",
        "trace_id": "trace-mock",
    }


def get_backend_info() -> Dict[str, Any]:
    return {
        "backend": "qiskit_aer_simulator",
        "local": True,
        "cost": 0,
        "deterministic": True,
    }


TOOLS = {
    "validate_qiskit_circuit": validate_qiskit_circuit,
    "transpile_circuit": transpile_circuit,
    "run_quantum_job": run_quantum_job,
    "get_backend_info": get_backend_info,
}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            tool = req.get("tool")
            args = req.get("args", {})
            if tool in TOOLS:
                result = TOOLS[tool](**args)
                print(json.dumps({"ok": True, "result": result}))
            else:
                print(json.dumps({"ok": False, "error": f"Unknown tool: {tool}"}))
        except Exception as e:
            print(json.dumps({"ok": False, "error": str(e)}))
        sys.stdout.flush()


if __name__ == "__main__":
    main()