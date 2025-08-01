# Australian House Price ETL & ML Pipeline

This repository contains a project to:

- Extract and transform historical Australian house price data (ABS + optional state-level data)
- Load the processed dataset into PostgreSQL
- Train forecasting models (Prophet, XGBoost) to predict future median house prices by state and suburb
- Serve predictions in an interactive dashboard (Streamlit or Dash)
- Automate the pipeline with optional components (Airflow, Docker, AWS deployment)

## 📁 Repo Structure
├── etl/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
├── data/
│ └── raw/ # raw CSV/XLSX downloaded
├── models/
│ ├── prophet_model.ipynb
│ └── xgb_model.ipynb
├── dashboard/
│ └── app.py # Streamlit dashboard
├── architecture.png # The architecture diagram
├── README.md
└── requirements.txt

---

## 🛠 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/justinminlee/house-price-pipeline.git
   cd house-price-pipeline
Install dependencies:
```
pip install -r requirements.txt
```
Download the ABS dataset:

Visit [ABS Residential Property Price Indexes][ABS]

Export time series data (median prices for eight capital cities)

Save to data/raw/abs_prices.xlsx

Run ETL:
```
python etl/extract.py
python etl/transform.py
python etl/load.py
```
Model training & prediction:

Launch Jupyter notebooks in models/

Run forecasting models and store outputs back to PostgreSQL

Serve dashboard:

bash
복사
편집
streamlit run dashboard/app.py
