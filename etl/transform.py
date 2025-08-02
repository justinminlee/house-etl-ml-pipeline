import pandas as pd
from extract_abs import extract_abs
from extract_sa import extract_sa

def normalise_state(state):
    state_map = {
        "nsw": "New South Wales",
        "vic": "Victoria",
        "qld": "Queensland",
        "sa": "South Australia",
        "wa": "Western Australia",
        "tas": "Tasmania",
        "nt": "Northern Territory",
        "act": "Australian Capital Territory",
        "national": "National"
    }
    return state_map.get(state.lower(), state)

def transform_data():
    print("[Transform] Starting data transformation...")

    # Extract ABS data
    df_abs = extract_abs()

    # Ensure state column exists for ABS dataset
    if "state" not in df_abs.columns:
        print("[Transform] Adding state column to ABS data")
        df_abs["state"] = "National"

    # Normalise state names
    df_abs["state"] = df_abs["state"].apply(normalise_state)

    # Convert date to datetime format
    if "date" in df_abs.columns:
        df_abs["date"] = pd.to_datetime(df_abs["date"], errors="coerce")

        # Filter out old records (before 2000)
        initial_count = len(df_abs)
        df_abs = df_abs[df_abs["date"].dt.year >= 2000]
        print(f"[Transform] Filtered ABS data: {initial_count} → {len(df_abs)} rows (2000 onwards)")

    # Extract SA data
    df_sa = extract_sa()
    df_sa["state"] = "South Australia"

    # Ensure SA date column is datetime
    if "date" in df_sa.columns:
        df_sa["date"] = pd.to_datetime(df_sa["date"], errors="coerce")
        df_sa = df_sa[df_sa["date"].dt.year >= 2000]

    # Merge datasets based on common columns
    common_cols = list(set(df_abs.columns) & set(df_sa.columns))
    df_combined = pd.concat([df_abs[common_cols], df_sa[common_cols]], ignore_index=True)

    print(f"[Transform] Combined dataset: {df_combined.shape[0]} rows after filtering")
    return df_combined
