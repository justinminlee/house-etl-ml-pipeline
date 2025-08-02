# Objective
 - To build an automated data pipeline and interactive dashboard to:

 - Analyze historical housing price trends across Australian states.

 - Assess the impact of migration and population growth on housing markets.

 - Generate data-driven hypotheses and visual insights.

 - Apply machine learning forecasting to predict future housing prices and identify potential high-growth areas.

# Data Sources
```
| Dataset                                 | Source | Table ID              | Purpose                                  |
| --------------------------------------- | ------ | --------------------- | ---------------------------------------- |
| Residential Property Price Index (RPPI) | ABS    | Tables 1–5            | Analyze historical price changes         |
| Median Price & Number of Transfers      | ABS    | Table 6               | Median property prices & market activity |
| Estimated Resident Population (ERP)     | ABS    | Table 4               | Population growth tracking               |
| Net Interstate Migration (NIM)          | ABS    | Table 4/supplementary | Migration trends affecting demand        |
```
# Hypothesis
 - We will test and visualize the following hypotheses:

 - Population Growth → Price Increase: States with higher population growth rates will experience faster housing price increases.

 - Migration-Driven Demand: Net interstate migration is positively correlated with housing price changes.

 - Price-Market Volume Relationship: Higher property transfers (market activity) lead to accelerated price growth.

 - State Variations: Housing prices grow at different rates across states due to economic and demographic factors.

# Machine Learning Component
 - Model: Time Series Forecasting (Prophet or XGBoost Regressor).

 - Target: Predict housing price index for each state.

 - Features: Population growth rate, net migration, previous price trends, and number of transfers.

 - Outcome: Future price projections (e.g. next 12 months) and state-level ranking for potential growth.

# Deliverables
- Automated ETL Pipeline
    - Scrape and download ABS datasets.
    - Transform and merge into a single analysis-ready dataset.

- Streamlit Dashboard
    - Interactive visualizations:
        - Price trends by state
        - Population growth vs price
        - Migration vs price correlation
        - Transfers and market activity

    - Hypotheses explanation with data-driven insights.
    - ML price forecasting with state-level future predictions.

- Documentation
    - Project proposal 
    - Data dictionary
    - Technical implementation notes
    - Insights and business recommendations

# Tools & Technologies
- Data Engineering: Python (Pandas, Requests, BeautifulSoup)

- Storage: CSV/Parquet

- Visualization: Streamlit, Plotly

- ML Forecasting: Prophet or Scikit-learn

- Version Control: Git/GitHub

- Deployment: Streamlit Cloud

# Project Timeline
```
| Phase                | Duration |
| -------------------- | -------- |
| Data Pipeline (ETL)  | 1 week   |
| Exploratory Analysis | 1 week   |
| ML Model Development | 1 week   |
| Streamlit Dashboard  | 1 week   |
| Testing & Deployment | 2–3 days |
```

---

## 🛠 Setup

1. Clone the repo:
   ```bash 
   git clone https://github.com/justinminlee/house-price-pipeline.git
   cd house-price-pipeline

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Download the ABS dataset:

- Visit [ABS Residential Property Price Indexes][ABS]

- Export time series data (median prices for eight capital cities)

- Save to data/raw/

4. Run ETL:
    ```
    python etl/extract.py
    python etl/transform.py
    python etl/load.py
    ```

5. Model training & prediction:

- Launch Jupyter notebooks in models/

- Run forecasting models and store outputs back to PostgreSQL

6. Serve dashboard:
    ```
    streamlit run dashboard/app.py
    ```