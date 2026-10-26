# On-Call Runbook

## Trigger
Alert: `quantum_job_failed` (job failed 3 times or latency p95 > threshold).

## Steps
1. Read alert payload (job_id, trace_id, failure_reason).
2. Query backend `GET /api/v1/jobs/{job_id}` for details.
3. If failure is due to refactored circuit:
   - `git revert HEAD~1 --no-commit`
   - Open PR with fix.
   - Notify monitoring channel.
4. If transient:
   - Retry job via `POST /api/v1/quantum-job`.
5. Close alert.