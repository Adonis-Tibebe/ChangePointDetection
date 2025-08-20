// src/components/ImpactAnalysis.js
import React from 'react';

const ImpactAnalysis = ({ impactData }) => {
  // Filter for significant impacts for display
  const significantImpacts = impactData.filter(
    impact => Math.abs(impact.price_change_pct) > 5 || Math.abs(impact.volatility_change_pct) > 20
  ).slice(0, 5); // Show top 5

  if (significantImpacts.length === 0) {
    return (
      <div className="impact-panel">
        <h2>Top Market Impacts</h2>
        <p>No significant impacts found in the data.</p>
      </div>
    );
  }

  return (
    <div className="impact-panel">
      <h2>Top Market Impacts</h2>
      <div className="impact-cards">
        {significantImpacts.map((impact, index) => (
          <div key={index} className="impact-card">
            <h3>Change on {new Date(impact.change_point_date).toLocaleDateString()}</h3>
            <div className="impact-metrics">
              <div className="metric">
                <span className="label">Price Change:</span>
                <span className={`value ${impact.price_change_pct >= 0 ? 'positive' : 'negative'}`}>
                  {impact.price_change_pct >= 0 ? '+' : ''}{impact.price_change_pct.toFixed(1)}%
                </span>
              </div>
              <div className="metric">
                <span className="label">Volatility Change:</span>
                <span className={`value ${impact.volatility_change_pct >= 0 ? 'positive' : 'negative'}`}>
                  {impact.volatility_change_pct >= 0 ? '+' : ''}{impact.volatility_change_pct.toFixed(1)}%
                </span>
              </div>
              <div className="metric">
                <span className="label">Price Before:</span>
                <span className="value">${impact.from_price?.toFixed(2)}</span>
              </div>
              <div className="metric">
                <span className="label">Price After:</span>
                <span className="value">${impact.to_price?.toFixed(2)}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ImpactAnalysis;