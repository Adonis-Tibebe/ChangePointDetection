// src/App.js
import React, { useState, useEffect } from 'react';
import PriceChart from './components/PriceChart';
import EventTable from './components/EventTable';
import ImpactAnalysis from './components/ImpactAnalysis';
import './App.css';

function App() {
  // State to hold all the data fetched from the backend
  const [priceData, setPriceData] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [events, setEvents] = useState([]);
  const [impactData, setImpactData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch all data from Flask backend on component mount
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        // Fetch all endpoints in parallel for better performance
        const [priceRes, pointsRes, eventsRes, impactRes] = await Promise.all([
          fetch('http://127.0.0.1:5000/api/price_data'),
          fetch('http://127.0.0.1:5000/api/change_points'),
          fetch('http://127.0.0.1:5000/api/events'),
          fetch('http://127.0.0.1:5000/api/impact_analysis')
        ]);

        // Check if any response failed
        if (!priceRes.ok || !pointsRes.ok || !eventsRes.ok || !impactRes.ok) {
          throw new Error('Failed to fetch data from server');
        }

        // Parse JSON responses
        const [priceJson, pointsJson, eventsJson, impactJson] = await Promise.all([
          priceRes.json(),
          pointsRes.json(),
          eventsRes.json(),
          impactRes.json()
        ]);

        // Update state with fetched data
        setPriceData(priceJson);
        setChangePoints(pointsJson);
        setEvents(eventsJson);
        setImpactData(impactJson);
        setError(null);
      } catch (err) {
        setError(err.message);
        console.error('Error fetching data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="App">
        <header className="App-header">
          <h1>Brent Crude Oil Price Analysis</h1>
        </header>
        <div className="loading">Loading data... Please wait.</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="App">
        <header className="App-header">
          <h1>Brent Crude Oil Price Analysis</h1>
        </header>
        <div className="error">
          <h2>Error Loading Data</h2>
          <p>{error}</p>
          <p>Make sure your Flask backend is running on http://localhost:5000</p>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Brent Crude Oil Price Analysis</h1>
        <p>Detected {changePoints.length} structural change points aligned with {events.filter(e => e.match_status === '✅ STRONG MATCH').length} major events</p>
      </header>

      <main className="dashboard-container">
        {/* Panel 1: Interactive Price Chart with overlays */}
        <section className="dashboard-panel full-width">
          <PriceChart 
            priceData={priceData} 
            changePoints={changePoints} 
            events={events}
          />
        </section>

        {/* Panel 2: Impact Analysis */}
        <section className="dashboard-panel">
          <ImpactAnalysis impactData={impactData} />
        </section>

        {/* Panel 3: Event Table */}
        <section className="dashboard-panel">
          <EventTable events={events} />
        </section>
      </main>
    </div>
  );
}

export default App;