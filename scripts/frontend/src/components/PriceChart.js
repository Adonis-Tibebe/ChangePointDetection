// src/components/PriceChart.js
import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Scatter } from 'recharts';

const PriceChart = ({ priceData, changePoints, events }) => {
  // Prepare event data for the scatter plot
  const eventData = events.map(event => {
    // Find the price on the event date for positioning
    const pricePoint = priceData.find(p => p.date === event.event_date) || {};
    return {
      ...event,
      // Use the event date and the price on that date for plotting
      x: new Date(event.event_date).getTime(), // Scatter needs numerical x values
      y: pricePoint.Price,
      value: pricePoint.Price // For tooltip display
    };
  });

  // Custom tooltip formatter
  const renderTooltip = (props) => {
    const { active, payload } = props;
    if (active && payload && payload.length) {
      const data = payload[0].payload;
      return (
        <div className="custom-tooltip">
          <p>{`Date: ${new Date(data.date || data.x).toLocaleDateString()}`}</p>
          <p>{`Price: $${data.Price?.toFixed(2) || data.value?.toFixed(2)}`}</p>
          {data.title && <p><strong>Event:</strong> {data.title}</p>}
          {data.match_status && <p><em>{data.match_status}</em></p>}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="chart-panel">
      <h2>Price History with Change Points & Events</h2>
      <ResponsiveContainer width="100%" height={500}>
        <LineChart
          data={priceData}
          margin={{ top: 20, right: 30, left: 20, bottom: 30 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="date" 
            tickFormatter={(tick) => new Date(tick).toLocaleDateString()}
            angle={-45}
            textAnchor="end"
            height={80}
          />
          <YAxis 
            domain={['auto', 'auto']}
            tickFormatter={(value) => `$${value}`}
          />
          <Tooltip content={renderTooltip} />
          <Legend />
          
          {/* Main Price Line */}
          <Line 
            type="monotone" 
            dataKey="Price" 
            stroke="#3366cc" 
            strokeWidth={2}
            dot={false}
            name="Brent Oil Price"
          />
          
          {/* Change Points as Scatter */}
          <Scatter
            data={changePoints}
            dataKey="price_at_cp"
            fill="red"
            shape={(props) => {
              const { payload, cx, cy } = props;
              return (
                <g>
                  <line
                    x1={cx}
                    y1={cy - 100} // Adjust based on your chart height
                    x2={cx}
                    y2={cy + 100}
                    stroke="red"
                    strokeWidth={2}
                    strokeDasharray="5 3"
                  />
                  <circle cx={cx} cy={cy} r={6} fill="red" stroke="#fff" strokeWidth={2} />
                </g>
              );
            }}
            name="Change Points"
          />
          
          {/* Events as Scatter */}
          <Scatter
            data={eventData}
            dataKey="value"
            fill="orange"
            shape={(props) => {
              const { cx, cy, payload } = props;
              let fillColor = '#ff9966'; // Default for weak matches
              if (payload.match_status === '✅ STRONG MATCH') fillColor = '#ff0000';
              if (payload.match_status === '❌ NO MATCH') fillColor = '#cccccc';
              
              return (
                <g>
                  <circle cx={cx} cy={cy} r={8} fill={fillColor} stroke="#fff" strokeWidth={2} />
                  <text x={cx} y={cy - 15} textAnchor="middle" fill={fillColor} fontSize={20}>
                    ●
                  </text>
                </g>
              );
            }}
            name="Geopolitical Events"
          />
        </LineChart>
      </ResponsiveContainer>
      
      <div className="chart-legend">
        <p><span style={{color: 'red'}}>●</span> Change Points | 
        <span style={{color: 'red'}}> ●</span> Strong Event Match | 
        <span style={{color: '#ff9966'}}> ●</span> Weak Event Match | 
        <span style={{color: '#cccccc'}}> ●</span> No Match</p>
      </div>
    </div>
  );
};

export default PriceChart;