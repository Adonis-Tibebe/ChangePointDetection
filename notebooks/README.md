# Notebooks Directory

This directory contains Jupyter notebooks for the Brent oil price change point detection analysis.

## Current State

### Available Notebooks
- `Data_ingestion.ipynb` - **COMPLETED** ✅ Data conversion and storage (JSON to CSV format)

**Current Functionality**:
- Converts structured JSON event data to CSV format for easier analysis
- Saves both JSON and CSV versions in `data/processed/` directory
- Contains 12 major geopolitical and economic events with comprehensive metadata
- Includes cross-validated event data with source links and impact estimates

**Key Features**:
- Event data spans from 1987 to 2022
- Covers multiple categories: OPEC decisions, conflicts, economic shocks, sanctions, supply shocks
- Each event includes start date, duration, impact direction, influence level, and source validation
- Data is ready for modeling and insight generation

## Planned Analysis Workflow

### 1. Data Ingestion & Exploration ✅ **COMPLETED**
**Notebook**: `Data_ingestion.ipynb` - Data conversion and storage

**Completed Tasks**:
- ✅ Converted JSON event data to DataFrame format
- ✅ Saved event data in both JSON and CSV formats
- ✅ Validated data structure and completeness
- ✅ Prepared 12 major events for analysis

**Next Steps for Data Loading**:
- Load Brent price data from `data/raw/BrentOilPrices_raw.csv`
- Perform initial data quality assessment
- Create basic visualizations of price trends
- Identify data gaps, outliers, and formatting issues

### 2. Exploratory Data Analysis (EDA)
**Planned Notebook**: `01_EDA_TimeSeries_Analysis.ipynb`

**Key Tasks**:
- Load both Brent price data and event data
- Time series visualization (raw prices and log returns)
- Distributional properties analysis
- Volatility clustering identification
- Stationarity and seasonality testing
- Rolling statistics computation

**Expected Outputs**:
- Comprehensive EDA report
- Volatility analysis plots
- Stationarity test results

### 3. Data Preprocessing & Feature Engineering
**Planned Notebook**: `02_Data_Preprocessing.ipynb`

**Key Tasks**:
- Handle missing data and outliers
- Create weekly/monthly aggregations
- Compute log differences and returns
- Add event flags and feature encoding
- Prepare data for modeling

**Expected Outputs**:
- Cleaned and feature-engineered datasets
- Preprocessing pipeline documentation

### 4. Change Point Detection Modeling
**Planned Notebook**: `03_ChangePoint_Detection.ipynb`

**Key Tasks**:
- Implement Bayesian change point detection
- Apply frequentist methods for comparison
- Model evaluation and diagnostics
- Posterior analysis and interpretation

**Expected Outputs**:
- Change point detection results
- Model comparison analysis
- Confidence intervals for detected changes

### 5. Event Impact Analysis
**Planned Notebook**: `04_Event_Impact_Analysis.ipynb`

**Key Tasks**:
- Match detected change points with events
- Quantify impact magnitudes and durations
- Pattern recognition and clustering
- Statistical significance testing

**Expected Outputs**:
- Event-impact mapping
- Impact quantification metrics
- Pattern analysis results

### 6. Visualization & Reporting
**Planned Notebook**: `05_Visualization_Dashboard.ipynb`

**Key Tasks**:
- Create interactive visualizations
- Generate annotated time series plots
- Build dashboard components
- Prepare final report figures

**Expected Outputs**:
- Interactive dashboard prototype
- Publication-ready visualizations
- Final analysis report

## Development Guidelines

### Notebook Structure
Each notebook should follow this structure:
1. **Setup & Imports** - Load required libraries and data
2. **Data Loading** - Import and validate data sources
3. **Analysis** - Main analytical work
4. **Visualization** - Create relevant plots and charts
5. **Summary** - Key findings and next steps

### Code Standards
- Use clear, descriptive variable names
- Include markdown cells for explanations
- Document assumptions and limitations
- Save intermediate results for reproducibility

### Output Management
- Save processed data to `data/processed/`
- Export results to `docs/reports/`

## Dependencies

Ensure the following packages are available:
- `pandas` for data manipulation
- `numpy` for numerical computations
- `matplotlib` and `seaborn` for visualization
- `scipy` and `statsmodels` for statistical analysis
- `pymc3` or `pymc` for Bayesian modeling
- `ruptures` for frequentist change point detection
- `json` for data format handling

## Next Steps

1. ✅ **COMPLETED**: Data ingestion and format conversion
2. Create the EDA notebook for comprehensive analysis
3. Build the preprocessing pipeline
4. Implement change point detection models
5. Conduct event impact analysis
6. Create final visualizations and dashboard
