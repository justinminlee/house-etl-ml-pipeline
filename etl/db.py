from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Date, Integer
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def create_tables():
    metadata = MetaData()

    house_prices = Table(
        "house_prices", metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("date", Date, nullable=False),
        Column("state", String, nullable=False),
        Column("suburb", String),
        Column("source", String),
        Column("property_type", String),
        Column("bedrooms", Integer),
        Column("median_price", Float, nullable=False),
        Column("price_change", Float),
        Column("rolling_avg", Float)
    )

    metadata.create_all(engine)
    print("[DB] Table 'house_prices' is ready.")

if __name__ == "__main__":
    create_tables()
