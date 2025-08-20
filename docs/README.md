# Brent Oil Price Change Point Detection - Documentation

## Project Overview

This project implements a comprehensive change point detection analysis for Brent crude oil prices from 1987-2022. The system identifies structural breaks in price patterns and correlates them with major geopolitical and economic events using both Bayesian and frequentist approaches.

## Architecture

### Core Components

#### 1. Data Pipeline (`data/`)
- **Raw Data**: Historical Brent oil price data (1987-2022, 9,013 daily observations)
- **Processed Data**: Transformed price data with calculated features
- **Event Data**: 12 major geopolitical events with metadata and source validation

#### 2. Analysis Engine (`src/`)
- **Models** (`src/models/`): Configuration classes for change point detection algorithms
- **Utils** (`src/utils/`): Core analysis functions for change point detection and event matching
- **Core** (`src/core/`): Base classes and interfaces

#### 3. Interactive Dashboard (`scripts/`)
- **Backend** (`scripts/backend/`): Flask API serving analysis results
- **Frontend** (`scripts/frontend/`): React application for data visualization

#### 4. Analysis Notebooks (`notebooks/`)
- **Data Ingestion**: Event data structuring and validation
- **EDA**: Exploratory data analysis and transformation
- **Change Point Detection**: Main analysis workflow

## Technical Implementation

### Change Point Detection Methods

#### Ruptures Library Implementation
- **Algorithm**: PELT (Pruned Exact Linear Time)
- **Cost Function**: Normal distribution (detects changes in mean and variance)
- **Parameters**:
  - Minimum segment size: 22 trading days
  - Jump parameter: 5 (for computation speed)
  - Penalty values tested: [2, 5, 10, 15, 20, 30, 35]
  - Primary penalty: 30 (optimal balance)

#### Bayesian Approach (PyMC)
- Single change point detection models
- Note: Limited effectiveness for multiple change points

### Data Processing Pipeline

#### Price Data Transformation
1. **Log Returns Calculation**: `log(price_t / price_{t-1})`
2. **Rolling Statistics**: 30-day mean and volatility windows
3. **Stationarity Testing**: ADF and KPSS tests
4. **Distribution Analysis**: Fat tails, skewness assessment

#### Event Matching Algorithm
- **Time Window**: 90 days maximum (configurable)
- **Match Categories**:
  - ✅ STRONG MATCH: ≤30 days proximity
  - ⚠️ WEAK MATCH: 31-90 days proximity
  - ❌ NO MATCH: >90 days proximity

### Statistical Analysis

#### Segment Statistics
- Duration (days)
- Mean and median prices
- Mean log returns (annualized)
- Volatility (annualized percentage)
- Number of observations

#### Impact Quantification
- Price change percentage between segments
- Volatility change percentage
- Before/after price and volatility values

## API Reference

### Backend Endpoints

#### Data Endpoints
- `GET /api/price_data` - Historical Brent oil price data
- `GET /api/change_points` - Detected change points with dates and indices
- `GET /api/segments` - Statistical analysis of price segments
- `GET /api/events` - Historical oil market events metadata

#### Analysis Endpoints
- `GET /api/strong_matches` - Events strongly correlated with change points
- `GET /api/impact_analysis` - Price and volatility impact analysis

### Frontend Components

#### PriceChart Component
- Interactive time series visualization
- Change point overlays (red dashed lines)
- Event annotations (orange dotted lines)
- Dual-panel view: prices and log returns

#### ImpactAnalysis Component
- Price change percentage displays
- Volatility change indicators
- Color-coded positive/negative impacts
- Responsive metric cards

#### EventTable Component
- Sortable event matching results
- Match status indicators
- Event categories and impact directions
- Date proximity calculations

## Data Schema

### Price Data Structure
```json
{
  "Date": "YYYY-MM-DD",
  "Price": "float",
  "Log_Return": "float"
}
```

### Event Data Structure
```json
{
  "title": "string",
  "start_date": "YYYY-MM-DD",
  "duration_weeks": "integer",
  "category": "string",
  "description": "string",
  "impact_direction": "up|down",
  "influence_level": "low|medium|high|very_high",
  "source_links": ["array of URLs"],
  "notes": "string"
}
```

### Change Point Results
```json
{
  "breakpoint_index": "integer",
  "date": "YYYY-MM-DD",
  "event_rank": "integer",
  "price_at_cp": "float"
}
```

## Configuration

### Change Point Detection Parameters
```python
class ChangePointConfig:
    cost_function = "normal"      # Detect mean and variance changes
    search_method = "Pelt"        # Pruned Exact Linear Time algorithm
    penalty_values = [2, 5, 10, 15, 20, 30, 35]
    min_segment_size = 22         # Minimum 1 month of trading days
    jump = 5                      # Computation speed optimization
    primary_penalty = 30          # Optimal penalty value
```

### Event Matching Configuration
- **Default Window**: 90 days maximum proximity
- **Strong Match Threshold**: ≤30 days
- **Weak Match Threshold**: 31-90 days
- **No Match**: >90 days

## Development Workflow

### Testing
```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/unit/test_ruptures_config.py
```

### Code Quality
```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Clean up
make clean
```

### Dashboard Development
```bash
# Install frontend dependencies
cd scripts/frontend && npm install

# Start development servers
make dashboard-backend    # Backend only
make dashboard-frontend   # Frontend only
make dashboard           # Both
```

## Key Results Summary

### Change Point Detection
- **Total Change Points**: 23 structural breaks over 35 years
- **Detection Method**: Ruptures PELT with normal cost function
- **Optimal Penalty**: 30 (balance of sensitivity and specificity)

### Event Correlation
- **Strong Matches**: 6 events with ≤30 days proximity
- **Weak Matches**: Multiple events with 31-90 days proximity
- **Categories**: OPEC decisions, conflicts, economic shocks, sanctions

### Data Quality
- **Time Coverage**: 12,919 days (1987-2022)
- **Data Points**: 9,013 daily observations
- **Missing Values**: Minimal, high-quality time series
- **Stationarity**: Log returns suitable for statistical modeling

## Performance Characteristics

### Computational Efficiency
- **PELT Algorithm**: O(n²) worst case, typically O(n log n)
- **Jump Parameter**: 5x speed improvement with minimal accuracy loss
- **Memory Usage**: Linear with data size

### Scalability
- **Data Size**: Tested up to 9,013 observations
- **Event Matching**: O(n×m) complexity (n change points, m events)
- **API Response**: Sub-second response times for typical queries

## Limitations and Considerations

### Algorithm Limitations
- **Ruptures**: Assumes piecewise constant models
- **PELT**: May miss gradual regime changes
- **Normal Cost**: Assumes Gaussian distribution within segments

### Data Limitations
- **Event Granularity**: Daily price data vs. event-level analysis
- **Causality**: Correlation does not imply causation
- **Market Efficiency**: Assumes markets reflect information quickly

### Model Assumptions
- **Stationarity**: Log returns assumed stationary within segments
- **Independence**: Price changes assumed independent between segments
- **Distribution**: Normal distribution within segments

## Future Enhancements

### Algorithm Improvements
- **Multiple Cost Functions**: Support for different distributional assumptions
- **Adaptive Penalties**: Dynamic penalty selection based on data characteristics
- **Gradual Changes**: Detection of smooth regime transitions

### Feature Additions
- **Real-time Updates**: Live data integration
- **Advanced Visualizations**: Interactive 3D plots, correlation matrices
- **Machine Learning**: Event prediction based on price patterns

### Performance Optimizations
- **Parallel Processing**: Multi-core change point detection
- **Caching**: API response caching for improved performance
- **Database Integration**: Persistent storage for large datasets
