# Brent Oil Price Change Point Detection

## Business Objective

The main goal of this analysis is to study how important events affect Brent oil prices. This will focus on finding out how changes in oil prices are linked to big events like political decisions, conflicts in oil-producing regions, global economic sanctions, and changes in Organization of the Petroleum Exporting Countries (OPEC) policies. The aim is to provide clear insights that can help investors, analysts, and policymakers understand and react to these price changes better.

## Project Overview

This project implements a comprehensive change point detection analysis for Brent crude oil prices from 1987-2022, identifying structural breaks in price patterns and correlating them with major geopolitical and economic events. The analysis uses both Bayesian and frequentist approaches to detect regime changes and quantify their impact on oil markets.

## Current Implementation Status

### ✅ Completed Components

1. **Data Pipeline**
   - Raw Brent oil price data ingestion (1987-2022, 9,013 daily observations)
   - Event data collection and structuring (12 major geopolitical events)
   - Data transformation and feature engineering
   - Comprehensive data quality assessment

2. **Exploratory Data Analysis**
   - Time series visualization with event annotations
   - Distributional analysis (fat tails, skewness)
   - Stationarity testing (ADF, KPSS)
   - Rolling statistics computation (30-day mean and volatility)

3. **Change Point Detection**
   - PyMC-based Bayesian models (single change point)
   - Ruptures library implementation (multiple change points)
   - Penalty selection using elbow method
   - 23 change points detected using penalty value 30

4. **Impact Analysis**
   - Segment statistics calculation (24 price segments)
   - Price and volatility change quantification
   - Event-change point matching algorithm
   - Strong match identification (≤30 days proximity)

5. **Results Export**
   - Comprehensive CSV outputs for further analysis
   - Change point detection results
   - Segment statistics and impact analysis
   - Event matching results

6. **Analytical Dashboard**
   - Interactive web dashboard for data visualization
   - Flask backend API serving analysis results
   - React frontend with interactive charts and tables
   - Real-time data exploration capabilities

### 📊 Key Results

- **Change Points Detected**: 23 structural breaks over 35 years
- **Strong Event Matches**: 6 events with high confidence (≤30 days)
- **Average Segment Duration**: 537 days
- **Time Period Analyzed**: 12,919 days (1987-2022)
- **Most Impactful Events**: Russia-Saudi price war & COVID crash
- **Detection Method**: Ruptures PELT algorithm with normal cost function

## Project Structure

```
ChangePointDetection/
├── data/
│   ├── raw/                    # Raw Brent oil price data (1987-2022)
│   └── processed/              # Processed data and analysis results
│       ├── oil_events.csv      # Event metadata
│       ├── BrentOilPrices_transformed.csv  # Transformed price data
│       └── change_point_detection_results/ # Analysis outputs
├── notebooks/                  # Jupyter notebooks for analysis
│   ├── Data_ingestion.ipynb   # Event data structuring
│   ├── EDA_and_Transformation.ipynb  # Exploratory analysis
│   └── Change_PointDetection_and_Impact_Analysis.ipynb  # Main analysis
├── src/                        # Source code modules
│   ├── models/                 # Change point detection configuration
│   └── utils/                  # Utility functions for analysis
├── scripts/                    # Analytical dashboard components
│   ├── backend/                # Flask API server
│   │   └── app.py             # RESTful API endpoints
│   └── frontend/              # React web application
│       ├── src/                # React components
│       └── package.json       # Frontend dependencies
├── tests/                      # Unit and integration tests
├── docs/                       # Documentation
├── examples/                   # Example usage
├── .github/workflows/          # CI/CD pipeline configuration
├── Makefile                    # Build and development commands
└── pyproject.toml             # Project configuration
```

## Data Sources

### Brent Oil Prices
- **Coverage**: Daily prices from May 20, 1987 to September 30, 2022
- **Records**: 9,013 daily observations
- **Source**: Historical Brent crude oil price data
- **Format**: CSV with Date and Price columns

### Event Data
- **Events**: 12 major geopolitical and economic events
- **Categories**: OPEC decisions, conflicts, economic shocks, sanctions, supply shocks
- **Metadata**: Start dates, duration estimates, impact direction, influence levels
- **Validation**: Cross-referenced with multiple reliable sources

## Technical Implementation

### Libraries and Dependencies
- **Data Manipulation**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Statistical Analysis**: scipy, statsmodels
- **Bayesian Modeling**: pymc, arviz
- **Change Point Detection**: ruptures
- **Data Processing**: json, os, sys
- **Web Framework**: Flask (backend), React (frontend)
- **Charts**: Recharts for interactive visualizations

### Change Point Detection Methods
1. **Bayesian Approach**: PyMC models for single change point detection
2. **Frequentist Approach**: Ruptures PELT algorithm for multiple change points
3. **Model Selection**: Penalty-based selection using elbow method
4. **Validation**: Event matching and impact quantification

### Analysis Workflow
1. **Data Preparation**: Ingestion, cleaning, and transformation
2. **Exploratory Analysis**: Visualization and statistical testing
3. **Model Implementation**: Change point detection algorithms
4. **Results Analysis**: Impact quantification and event correlation
5. **Output Generation**: Comprehensive results export
6. **Dashboard Deployment**: Web-based interactive exploration

## Key Findings

### Model Performance
- PyMC struggled with multiple change points due to convergence issues
- Ruptures provided robust and scalable results for multiple regime detection
- Penalty value 30 offered optimal balance between sensitivity and specificity

### Event Correlation
- Strong alignment between detected change points and major geopolitical events
- 6 out of 23 change points strongly correlated with historical events
- Clear volatility regime shifts during crisis periods (2008, 2020)

### Data Quality
- High-quality time series with minimal missing values
- Clear event annotations with validated source information
- Stationary log returns suitable for statistical modeling

## Installation

```bash
# Clone the repository
git clone [repository-url]
cd ChangePointDetection

# Install Python dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd scripts/frontend
npm install
```

## Usage

### Running the Analysis

1. **Data Ingestion**: Execute `notebooks/Data_ingestion.ipynb` to prepare event data
2. **Exploratory Analysis**: Run `notebooks/EDA_and_Transformation.ipynb` for data profiling
3. **Change Point Detection**: Execute `notebooks/Change_PointDetection_and_Impact_Analysis.ipynb` for main analysis

### Running the Dashboard

1. **Start Backend**: Navigate to `scripts/backend/` and run `python app.py`
2. **Start Frontend**: Navigate to `scripts/frontend/` and run `npm start`
3. **Access Dashboard**: Open browser to `http://localhost:3000`

### Output Files

The analysis generates comprehensive results in `data/processed/change_point_detection_results/`:
- `change_point_results.csv`: Detected change points with dates and indices
- `segment_statistics.csv`: Statistical summary of price segments
- `change_impact_analysis.csv`: Impact analysis between segments
- `event_matching_results.csv`: Event-change point correlation

## Development

### Testing
```bash
# Run unit tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Or use Makefile
make test
make test-cov
```

### Code Quality
```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Or use Makefile
make format
make lint
```

### Development Setup
```bash
# Install development dependencies
make install-dev

# Clean up generated files
make clean
```

## Contributing

Please read the documentation in the `docs/` directory for development guidelines.

## License

[Add your license information here]
