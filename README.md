# Australian House Price ETL & ML Pipeline

This repository contains a project to:

- Extract and transform historical Australian house price data (ABS + optional state-level data)
- Load the processed dataset into PostgreSQL
- Train forecasting models (Prophet, XGBoost) to predict future median house prices by state and suburb
- Serve predictions in an interactive dashboard (Streamlit or Dash)
- Automate the pipeline with optional components (Airflow, Docker, AWS deployment)

## 📁 Repo Structure
├── etl/
ㅣ
│ ├── extract.py
ㅣ
│ ├── transform.py
ㅣ
│ └── load.py
ㅣ
├── data/
ㅣ
│ └── raw/ # raw CSV/XLSX downloaded
ㅣ
├── models/
ㅣ
│ ├── prophet_model.ipynb
ㅣ
│ └── xgb_model.ipynb
ㅣ
├── dashboard/
ㅣ
│ └── app.py # Streamlit dashboard
ㅣ
├── architecture.png # The architecture diagram
ㅣ
├── README.md
ㅣ
└── requirements.txt

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

- Save to data/raw/abs_prices.xlsx

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