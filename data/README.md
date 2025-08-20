# Data Directory

This directory contains all data files used in the Brent oil price change point detection analysis.

## Directory Structure

```
data/
├── raw/                    # Raw data files
│   └── BrentOilPrices_raw.csv  # Daily Brent oil prices (1987-2022)
└── processed/              # Processed and feature-engineered data
    ├── oil_events.csv      # Event metadata in CSV format
    ├── oil_events.json     # Event metadata in JSON format
    ├── BrentOilPrices_transformed.csv  # Transformed price data with features
    └── change_point_detection_results/ # Analysis results
        ├── change_point_results.csv     # Detected change points
        ├── segment_statistics.csv       # Statistical analysis of segments
        ├── change_impact_analysis.csv   # Impact analysis between segments
        └── event_matching_results.csv   # Event-change point matching
```

## Data Sources

### Brent Oil Price Time Series (`raw/BrentOilPrices_raw.csv`)

**Coverage**: Daily Brent crude oil prices from May 20, 1987 to September 30, 2022  
**Records**: 9,013 daily observations  
**Fields**:
- `Date`: Formatted as DD-MMM-YY (e.g., 20-May-87)
- `Price`: Brent oil price in USD per barrel

**Purpose**: Primary time series for analyzing price trends and detecting structural shifts caused by major political, economic, and geopolitical events.

### Transformed Price Data (`processed/BrentOilPrices_transformed.csv`)

**Content**: Enhanced price data with engineered features  
**Records**: 8,981 observations (after transformation)  
**Fields**:
- `Date`: Date in datetime format
- `Price`: Original Brent oil price
- `Log_Return`: Log returns (log(Price_t / Price_{t-1}))
- `Rolling_Mean`: 30-day rolling mean of prices
- `Rolling_Std_Log`: 30-day rolling standard deviation of log returns

**Purpose**: Preprocessed data ready for change point detection and statistical analysis.

### Event Data (`processed/oil_events.csv` and `processed/oil_events.json`)

**Content**: 12 major geopolitical and economic events with comprehensive metadata  
**Source Selection Criteria**:
1. Events begin after dataset start date (May 20, 1987)
2. Have credible price impact mechanisms (conflict, production cut, economic shock, sanctions)
3. Represent structural shifts persisting for several weeks or months
4. Verified via at least two reliable sources
5. Limited to high-relevance events across categories

**Event Categories**:
- **OPEC Decisions**: Quota breakdowns, production cuts, policy changes
- **Conflicts**: Iraq-Kuwait invasion, Libyan civil war, Saudi drone attacks
- **Economic Shocks**: Asian financial crisis, Global Financial Crisis, COVID-19
- **International Sanctions**: Iranian oil export restrictions
- **Supply Shocks**: US shale surge, OPEC+ production agreements

**Metadata Fields**:
- `title`: Event name and description
- `start_date`: Event start date (YYYY-MM-DD)
- `duration_weeks`: Estimated impact duration in weeks
- `category`: Event classification
- `description`: Detailed event description
- `impact_direction`: Price impact direction (up/down)
- `influence_level`: Impact magnitude (medium/high/very_high)
- `source_links`: Reference sources for validation
- `notes`: Additional context and validation notes

### Analysis Results (`processed/change_point_detection_results/`)

**Content**: Output files from change point detection analysis  
**Files**:
- `change_point_results.csv`: 23 detected change points with dates and indices
- `segment_statistics.csv`: Statistical summary of 24 price segments
- `change_impact_analysis.csv`: Price and volatility changes between segments
- `event_matching_results.csv`: Matching between change points and historical events

## Data Quality Assessment

### Brent Price Data
- **Completeness**: Daily coverage with minimal gaps
- **Format Consistency**: Standardized date format throughout
- **Outlier Detection**: Extreme values validated against external references

### Event Data
- **Source Reliability**: Events sourced from official EIA/IEA and OPEC publications
- **Cross-Validation**: Multiple LLM validation (ChatGPT, Deep Seek) with insights captured in notes
- **Limitations**: Start dates and durations are estimates; some events may overlap

### Transformed Data
- **Feature Engineering**: Log returns, rolling statistics, and volatility measures
- **Data Cleaning**: Handled missing values and date parsing issues
- **Stationarity**: Log returns confirmed stationary through ADF/KPSS tests

## Data Preprocessing Workflow

1. **Missing Data Handling**: Interpolate short gaps, flag longer gaps
2. **Date Parsing**: Convert string dates to datetime objects, handle non-standard separators
3. **Feature Engineering**: Compute log returns, rolling means, and volatility measures
4. **Data Validation**: Stationarity tests and distribution analysis
5. **Export**: Save transformed data for modeling

## Usage in Analysis

- **Exploratory Analysis**: Visualize price trends and identify volatility clusters
- **Change Point Detection**: Use as input for ruptures-based CPD models
- **Event Impact Quantification**: Measure price shifts and duration effects
- **Pattern Recognition**: Identify recurring themes and impact profiles

## Current Status

✅ **Completed**:
- Raw data ingestion and validation
- Event data collection and structuring
- Data transformation and feature engineering
- Change point detection analysis
- Results export and documentation

📊 **Analysis Results**:
- 23 change points detected using penalty value 30
- 6 strong event matches (≤30 days) identified
- Average segment duration: 537 days
- Time period analyzed: 12,919 days (1987-2022)
