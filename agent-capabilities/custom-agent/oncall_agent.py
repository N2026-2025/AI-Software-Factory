"""On-call agent skeleton: wakes on alert, executes runbook, opens PR."""

import json
import sys
import subprocess
from pathlib import Path


def load_alert(alert_path: str) -> dict:
    with open(alert_path) as f:
        return json.load(f)


def runbook_revert_faulty_refactor(commit_hash: str) -> str:
    """Simulates git revert of a bad refactor commit."""
    result = subprocess.run(["git", "revert", "--no-commit", commit_hash], capture_output=True, text=True)
    return result.stdout or result.stderr


def open_fix_pr(branch_name: str, message: str) -> str:
    """Simulates opening a PR on GitHub (skeleton)."""
    return f"PR opened on branch {branch_name}: {message}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python oncall_agent.py <alert.json>")
        sys.exit(1)

    alert = load_alert(sys.argv[1])
    print(f"[ON-CALL] Alert received: {alert.get('severity')} - {alert.get('message')}")

    if alert.get("source") == "quantum_job_failed":
        job_id = alert.get("job_id")
        print(f"[ON-CALL] Investigating job {job_id}")
        # Simulated remediation
        revert_output = runbook_revert_faulty_refactor("HEAD~1")
        print(f"[ON-CALL] Revert output: {revert_output[:200]}")
        pr = open_fix_pr(f"fix/quantum-job-{job_id}", f"Revert faulty refactor for job {job_id}")
        print(f"[ON-CALL] {pr}")
        print("[ON-CALL] Incident mitigated.")
    else:
        print("[ON-CALL] Unknown alert type, no runbook matched.")


if __name__ == "__main__":
    main()