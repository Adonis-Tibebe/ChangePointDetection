# Scripts

This directory contains the analytical dashboard components for the Brent Oil Price Change Point Detection project.

## Components

### Backend (`backend/`)
- **Flask API** (`app.py`) - RESTful API serving change point detection results, oil events, and impact analysis data
- Provides endpoints for price data, change points, segments, events, and strong matches

### Frontend (`frontend/`)
- **React Application** - Interactive web dashboard for visualizing change point detection results
- Components include:
  - Price charts with change point overlays
  - Impact analysis panels
  - Event matching tables
  - Interactive data exploration

## Usage

1. **Start Backend**: Navigate to `backend/` and run `python app.py`
2. **Start Frontend**: Navigate to `frontend/` and run `npm start`
3. **Access Dashboard**: Open browser to `http://localhost:3000`

## API Endpoints

- `/api/price_data` - Historical Brent oil price data
- `/api/change_points` - Detected change points
- `/api/segments` - Statistical analysis of price segments
- `/api/events` - Historical oil market events
- `/api/strong_matches` - Events strongly correlated with change points
- `/api/impact_analysis` - Price and volatility impact analysis
