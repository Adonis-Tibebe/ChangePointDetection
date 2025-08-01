# Data Directory

This directory contains all data files used in the Brent oil price change point detection analysis.

## Directory Structure

```
data/
├── raw/                    # Raw data files
│   └── BrentOilPrices_raw.csv  # Daily Brent oil prices (1987-2022)
└── processed/              # Processed and feature-engineered data
    ├── oil_events.csv      # Event metadata in CSV format
    └── oil_events.json     # Event metadata in JSON format
```

## Data Sources

### Brent Oil Price Time Series (`raw/BrentOilPrices_raw.csv`)

**Coverage**: Daily Brent crude oil prices from May 20, 1987 to September 30, 2022  
**Records**: 9,013 daily observations  
**Fields**:
- `Date`: Formatted as DD-MMM-YY (e.g., 20-May-87)
- `Price`: Brent oil price in USD per barrel

**Purpose**: Primary time series for analyzing price trends and detecting structural shifts caused by major political, economic, and geopolitical events.

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

## Data Quality Assessment

### Brent Price Data
- **Completeness**: Daily coverage with minimal gaps
- **Format Consistency**: Standardized date format throughout
- **Outlier Detection**: Extreme values validated against external references

### Event Data
- **Source Reliability**: Events sourced from official EIA/IEA and OPEC publications
- **Cross-Validation**: Multiple LLM validation (ChatGPT, Deep Seek) with insights captured in notes
- **Limitations**: Start dates and durations are estimates; some events may overlap

## Data Preprocessing Workflow

1. **Missing Data Handling**: Interpolate short gaps, flag longer gaps
2. **Aggregation**: Create weekly and monthly aggregates for different analysis granularities
3. **Transformations**: Compute log differences (returns) for stationarity
4. **Feature Engineering**: Add event flags and encode event types for modeling
5. **Event Annotation**: Match events to time series for post-modeling analysis

## Usage in Analysis

- **Exploratory Analysis**: Visualize price trends and identify volatility clusters
- **Change Point Detection**: Use as input for Bayesian and frequentist CPD models
- **Event Impact Quantification**: Measure price shifts and duration effects
- **Pattern Recognition**: Identify recurring themes and impact profiles

## Future Enhancements

- Add empirical effect size calculations (price/volatility shift magnitudes)
- Refine duration windows to match credible intervals
- Encode causal details and generate confidence scores
- Create interactive visualizations for dashboard presentation
