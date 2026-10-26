#!/usr/bin/env bash
# Pre-commit guardrail: prevent secrets and enforce contract-first

set -e

echo "Running pre-commit guardrails..."

# 1. Block commits containing real API tokens
if grep -riE "sk-|IBM_QUANTUM_TOKEN|OPENROUTER_API_KEY" --include="*.py" --include="*.md" --include="*.yaml" --include="*.yml" . ; then
  echo "ERROR: Potential secret detected in committed files."
  exit 1
fi

# 2. Validate openapi.yaml exists and is non-empty
if [ ! -f openapi.yaml ] || [ ! -s openapi.yaml ]; then
  echo "ERROR: openapi.yaml is missing or empty. Contract-first required."
  exit 1
fi

# 3. Run backend tests
cd backend && pip install -q -r requirements.txt && pytest

echo "All guardrails passed."