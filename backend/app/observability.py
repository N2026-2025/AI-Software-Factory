from fastapi import Request, Response
import uuid
import time
import json
import sys
from typing import Callable


def setup_trace_middleware(app):
    @app.middleware("http")
    async def trace_middleware(request: Request, call_next: Callable):
        trace_id = request.headers.get("x-trace-id") or str(uuid.uuid4())
        request.state.trace_id = trace_id
        start_time = time.time()

        response: Response = await call_next(request)

        duration = (time.time() - start_time) * 1000
        log = {
            "trace_id": trace_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": round(duration, 2),
        }
        print(json.dumps(log), file=sys.stdout)

        response.headers["x-trace-id"] = trace_id
        return response