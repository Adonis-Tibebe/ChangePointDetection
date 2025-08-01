# Brent Oil Price Change Point Detection

## Business Objective

The main goal of this analysis is to study how important events affect Brent oil prices. This will focus on finding out how changes in oil prices are linked to big events like political decisions, conflicts in oil-producing regions, global economic sanctions, and changes in Organization of the Petroleum Exporting Countries (OPEC) policies. The aim is to provide clear insights that can help investors, analysts, and policymakers understand and react to these price changes better.

### Situational Overview

You are a data scientist at Birhan Energies, a leading consultancy firm specialising in providing data-driven insights and strategic advice to stakeholders in the energy sector. With a mission to help clients navigate the complexities of the global energy market, Birhan Energies focuses on delivering actionable intelligence that supports decision-making processes for investors, policymakers, and energy companies.

You are tasked with analyzing how big political and economic events affect Brent oil prices. Understand how political decisions, conflicts in oil-producing areas, international sanctions, and OPEC policy changes affect the market.

The oil market is very unstable. This makes it hard for investors to make good decisions, manage risks, and maximize returns. Policymakers need detailed analysis to create strategies for economic stability and energy security. Energy companies need accurate price forecasts to plan operations, control costs, and secure supply chains.

As a data scientist at Birhan Energies, you are tasked with:

- Finding key events that have significantly impacted Brent oil prices over the past decade.
- Measuring how much these events affect price changes.
- Providing clear, data-driven insights to guide investment strategies, policy development, and operational planning.

## Data Analysis Workflow Overview

This project follows a comprehensive data analysis workflow:

1. **Business Understanding** - Define objectives, stakeholders, and success criteria
2. **Data Acquisition** - Collect Brent price time series and event data
3. **Exploratory Data Analysis** - Visualize and profile the data
4. **Data Preprocessing** - Handle missing data, create features, and prepare for modeling
5. **Modeling** - Implement Bayesian change point detection and alternative methods
6. **Post-Model Analysis** - Interpret results and quantify impacts
7. **Communication & Deployment** - Create interactive dashboard and reports

## Project Structure

```
ChangePointDetection/
├── data/
│   ├── raw/                    # Raw Brent oil price data (1987-2022)
│   └── processed/              # Processed event data and features
├── notebooks/                  # Jupyter notebooks for analysis
├── src/                        # Source code modules
│   ├── core/                   # Core functionality
│   ├── models/                 # Change point detection models
│   ├── services/               # Data services
│   └── utils/                  # Utility functions
├── tests/                      # Unit and integration tests
├── docs/                       # Documentation
├── examples/                   # Example usage
└── scripts/                    # Utility scripts
```

## Current State

### Data Available
- **Brent Oil Prices**: Daily time series from May 20, 1987 to September 30, 2022 (9,013 records)
- **Event Data**: 12 major geopolitical and economic events with metadata including:
  - Event titles and descriptions
  - Start dates and duration estimates
  - Impact direction (up/down) and influence levels
  - Source links and validation notes

### Key Events Included
- OPEC quota breakdowns and production decisions
- Major conflicts (Iraq-Kuwait, Libya civil war, Saudi drone attacks)
- Economic shocks (Asian financial crisis, Global Financial Crisis, COVID-19)
- International sanctions (Iran oil export sanctions)
- Supply shocks (US shale surge, OPEC+ production cuts)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. **Data Exploration**: Start with the notebooks in the `notebooks/` directory
2. **Model Development**: Use the modules in `src/` for change point detection
3. **Analysis**: Follow the data analysis workflow outlined above

## Expected Outputs

- Change Point Summary Table with dates, confidence intervals, and matched events
- Annotated time series plots with event markers
- Interactive dashboard for exploration
- Final report with key findings and recommendations

## Contributing

Please read the documentation in the `docs/` directory for development guidelines.

## License

[Add your license information here]
