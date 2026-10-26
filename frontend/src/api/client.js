const API_BASE = '/api/v1'

export async function refactorCircuit(sourceCode) {
  const res = await fetch(`${API_BASE}/refactor`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ source_code: sourceCode }),
  })
  if (!res.ok) throw new Error(await res.text())
  return res.json()
}

export async function submitJob(circuitVersionId, shots = 1024) {
  const res = await fetch(`${API_BASE}/quantum-job`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ circuit_version_id: circuitVersionId, shots }),
  })
  if (!res.ok) throw new Error(await res.text())
  return res.json()
}

export async function getJob(jobId) {
  const res = await fetch(`${API_BASE}/jobs/${jobId}`)
  if (!res.ok) throw new Error(await res.text())
  return res.json()
}