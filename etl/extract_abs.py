import pandas as pd

def extract_abs():
    abs_file = "data/raw/abs_house_prices.xlsx"
    print(f"[Extract ABS] Reading {abs_file}")

    xls = pd.ExcelFile(abs_file)
    print(f"[Extract ABS] Sheets: {xls.sheet_names}")

    # Pick the sheet containing house price data
    # ABS often names it "Data1" or "Table 4"
    sheet_name = None
    for candidate in ["Table 4", "Data1", "Data"]:
        if candidate in xls.sheet_names:
            sheet_name = candidate
            break

    if sheet_name is None:
        raise ValueError("Could not find a suitable sheet for ABS data")

    df = pd.read_excel(xls, sheet_name=sheet_name)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Standardize expected columns
    # Assume ABS data contains "Date", "State", "Median Price" or similar
    rename_map = {}
    if "date" not in df.columns:
        # Try to detect date column dynamically
        date_col = next((c for c in df.columns if "date" in c or "quarter" in c), None)
        if date_col:
            rename_map[date_col] = "date"

    if "state" not in df.columns:
        state_col = next((c for c in df.columns if "state" in c or "city" in c), None)
        if state_col:
            rename_map[state_col] = "state"

    if "median_price" not in df.columns:
        price_col = next((c for c in df.columns if "price" in c or "value" in c), None)
        if price_col:
            rename_map[price_col] = "median_price"

    df = df.rename(columns=rename_map)

    # Filter required columns
    required_cols = ["date", "state", "median_price"]
    df = df[[c for c in required_cols if c in df.columns]]

    print(f"[Extract ABS] Extracted {df.shape[0]} rows")
    return df
