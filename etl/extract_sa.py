import pandas as pd

def extract_sa():
    sa_file = "data/raw/sa_suburb_prices.csv"
    print(f"[Extract SA] Reading {sa_file}")

    df = pd.read_csv(sa_file)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Dynamically detect columns
    rename_map = {}

    # Detect date column
    date_col = next((c for c in df.columns if "date" in c or "quarter" in c or "period" in c or "year" in c), None)
    if date_col:
        rename_map[date_col] = "date"

    # Detect suburb/region column
    suburb_col = next((c for c in df.columns if "suburb" in c or "region" in c or "location" in c), None)
    if suburb_col:
        rename_map[suburb_col] = "suburb"

    # Detect price column
    price_col = next((c for c in df.columns if "price" in c or "median" in c or "value" in c), None)
    if price_col:
        rename_map[price_col] = "median_price"

    df = df.rename(columns=rename_map)

    # Convert date to datetime if available
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    else:
        print("[Extract SA] No date column found; using index as date placeholder")
        df["date"] = pd.date_range(start="2000-01-01", periods=len(df), freq="Q")

    # Keep only relevant columns
    required_cols = ["date", "suburb", "median_price"]
    df = df[[c for c in required_cols if c in df.columns]]

    print(f"[Extract SA] Extracted {df.shape[0]} rows")
    return df
