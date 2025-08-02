from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()

def get_engine():
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    DB = os.getenv("DB_NAME")
    if not all([USER, PASSWORD, HOST, PORT, DB]):
        raise ValueError("Database configuration is incomplete. Please check your environment variables.")
    engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")
    return engine