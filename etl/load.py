from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASS")
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    DB = os.getenv("DB_NAME")
    if not all([USER, PASSWORD, HOST, PORT, DB]):
        raise ValueError("Database configuration is incomplete. Please check your environment variables.")
    
    engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")
    return engine

def load_to_postgres(df, table_name):
    engine = get_engine()
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"[Load] Uploaded {len(df)} rows into {table_name}")

def load_all():
    # Load RPPI
    df_rppi = pd.read_csv("data/processed/rppi.csv")
    load_to_postgres(df_rppi, "rppi")

    # Load Median Transfers
    df_median = pd.read_csv("data/processed/median_transfers.csv")
    load_to_postgres(df_median, "median_transfers")

    # Load Population
    df_population = pd.read_csv("data/processed/population.csv")
    load_to_postgres(df_population, "population")

    # Load Net Migration
    df_migration = pd.read_csv("data/processed/net_migration.csv")
    load_to_postgres(df_migration, "net_migration")

if __name__ == "__main__":
    load_all()