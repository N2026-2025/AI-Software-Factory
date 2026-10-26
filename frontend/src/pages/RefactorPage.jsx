import { useState } from 'react'
import { refactorCircuit } from '../api/client'

export default function RefactorPage() {
  const [code, setCode] = useState('from qiskit import QuantumCircuit\nqc = QuantumCircuit(2)\nqc.h(0)\nqc.cx(0,1)\n')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    setLoading(true)
    try {
      const data = await refactorCircuit(code)
      setResult(data)
    } catch (err) {
      alert('Error: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h2>Refactor Qiskit Circuit</h2>
      <form onSubmit={handleSubmit}>
        <textarea value={code} onChange={e => setCode(e.target.value)} rows={10} style={{ width: '100%' }} />
        <button type="submit" disabled={loading}>
          {loading ? 'Refactoring...' : 'Refactor'}
        </button>
      </form>
      {result && (
        <div style={{ marginTop: 20, border: '1px solid #ccc', padding: 10 }}>
          <h3>Result</h3>
          <p>Version ID: {result.version_id}</p>
          <p>Depth: {result.depth}</p>
          <p>Gate count: {result.gate_count}</p>
          <p>Qubit count: {result.qubit_count}</p>
        </div>
      )}
    </div>
  )
}