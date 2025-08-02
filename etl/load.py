from transform import transform_data
from db import engine, create_tables
import pandas as pd

def load_data():
    print("[Load] Starting ETL...")
    create_tables()  # Ensure table exists

    df = transform_data()

    # Load into PostgreSQL
    df.to_sql("house_prices", engine, if_exists="append", index=False)
    print(f"[Load] Inserted {len(df)} rows into house_prices table.")
    print("[Load] ETL process completed successfully.")
if __name__ == "__main__":
    load_data()
