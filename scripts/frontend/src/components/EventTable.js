// src/components/EventTable.js
import React, { useState } from 'react';

const EventTable = ({ events }) => {
  const [sortConfig, setSortConfig] = useState({ key: 'event_date', direction: 'desc' });

  const sortedEvents = [...events].sort((a, b) => {
    if (a[sortConfig.key] < b[sortConfig.key]) {
      return sortConfig.direction === 'asc' ? -1 : 1;
    }
    if (a[sortConfig.key] > b[sortConfig.key]) {
      return sortConfig.direction === 'asc' ? 1 : -1;
    }
    return 0;
  });

  const requestSort = (key) => {
    let direction = 'asc';
    if (sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc';
    }
    setSortConfig({ key, direction });
  };

  return (
    <div className="event-panel">
      <h2>Geopolitical Events & Matches</h2>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th onClick={() => requestSort('event_date')}>Date</th>
              <th onClick={() => requestSort('title')}>Event</th>
              <th onClick={() => requestSort('category')}>Category</th>
              <th onClick={() => requestSort('match_status')}>Match Status</th>
              <th onClick={() => requestSort('days_difference')}>Days Diff</th>
            </tr>
          </thead>
          <tbody>
            {sortedEvents.map((event, index) => (
              <tr key={index} className={event.match_status === '✅ STRONG MATCH' ? 'strong-match' : ''}>
                <td>{new Date(event.event_date).toLocaleDateString()}</td>
                <td className="event-title">{event.title}</td>
                <td>{event.category}</td>
                <td className={`match-status ${event.match_status.includes('STRONG') ? 'strong' : 
                               event.match_status.includes('WEAK') ? 'weak' : 'none'}`}>
                  {event.match_status}
                </td>
                <td>{event.days_difference}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default EventTable;