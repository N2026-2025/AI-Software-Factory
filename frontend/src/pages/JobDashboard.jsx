import { useState, useEffect } from 'react'
import { submitJob, getJob } from '../api/client'

export default function JobDashboard() {
  const [jobs, setJobs] = useState([])
  const [versionId, setVersionId] = useState('')

  async function handleSubmit() {
    const job = await submitJob(versionId)
    setJobs([...jobs, job])
  }

  return (
    <div>
      <h2>Quantum Job Dashboard</h2>
      <div>
        <input value={versionId} onChange={e => setVersionId(e.target.value)} placeholder="Circuit version ID" />
        <button onClick={handleSubmit}>Run Job</button>
      </div>
      <ul>
        {jobs.map(j => (
          <li key={j.job_id}>
            Job {j.job_id.slice(0, 8)} — {j.status} — trace: {j.trace_id}
          </li>
        ))}
      </ul>
    </div>
  )
}