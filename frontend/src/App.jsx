import { useState } from 'react'
import RefactorPage from './pages/RefactorPage'
import JobDashboard from './pages/JobDashboard'

export default function App() {
  const [tab, setTab] = useState('refactor')
  return (
    <div style={{ fontFamily: 'sans-serif', padding: 20 }}>
      <h1>Quantum Data Factory</h1>
      <div style={{ marginBottom: 20 }}>
        <button onClick={() => setTab('refactor')} style={{ marginRight: 10 }}>
          Refactor Circuit
        </button>
        <button onClick={() => setTab('dashboard')}>Job Dashboard</button>
      </div>
      {tab === 'refactor' ? <RefactorPage /> : <JobDashboard />}
    </div>
  )
}