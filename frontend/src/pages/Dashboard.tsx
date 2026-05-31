import { useEffect, useState } from 'react';

interface StatusData {
  status: string;
  service: string;
}

function Dashboard() {
  const [status, setStatus] = useState<StatusData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('/api/status')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Status request failed: ${response.status}`);
        }
        return response.json();
      })
      .then((data: StatusData) => setStatus(data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <main className="dashboard-page">
      <section className="dashboard-card">
        <h1>OpsPilotAI Dashboard</h1>
        <p>Welcome to the dashboard. This page connects to the backend API.</p>

        {error ? (
          <div className="dashboard-error">Error: {error}</div>
        ) : status ? (
          <div className="dashboard-status">
            <p><strong>Service:</strong> {status.service}</p>
            <p><strong>Status:</strong> {status.status}</p>
          </div>
        ) : (
          <div className="dashboard-loading">Loading status...</div>
        )}
      </section>
    </main>
  );
}

export default Dashboard;
