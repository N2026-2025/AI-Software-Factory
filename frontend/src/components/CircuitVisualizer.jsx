export default function CircuitVisualizer({ qasm }) {
  return (
    <div style={{ border: '1px solid #ddd', padding: 10, fontFamily: 'monospace', fontSize: 12 }}>
      <h3>Circuit QASM</h3>
      <pre>{qasm || 'No circuit available'}</pre>
    </div>
  )
}