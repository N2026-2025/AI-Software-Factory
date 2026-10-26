export default function HistogramChart({ counts }) {
  const entries = counts ? Object.entries(counts) : []
  return (
    <div style={{ border: '1px solid #ddd', padding: 10 }}>
      <h3>Counts Histogram</h3>
      <div style={{ display: 'flex', gap: 10, alignItems: 'flex-end', height: 200 }}>
        {entries.map(([state, count]) => (
          <div key={state} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div style={{ height: count, width: 30, background: '#4f46e5' }} />
            <span>{state}</span>
          </div>
        ))}
      </div>
    </div>
  )
}