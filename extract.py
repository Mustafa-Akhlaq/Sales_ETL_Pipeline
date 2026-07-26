import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config import DB_CONFIG
from logger import logger


def extract_csv():
    try:
        north = pd.read_csv("data/sales_north.csv")
        south = pd.read_csv("data/sales_south.csv")
        east = pd.read_csv("data/sales_east.csv")

        sales = pd.concat([north, south, east], ignore_index=True)

        logger.info("CSV files extracted successfully.")

        return sales

    except Exception as e:
        logger.error(f"Error extracting CSV files: {e}")
        raise


def extract_customers():
    try:
        url = URL.create(
            drivername="postgresql+psycopg2",
            username=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            database=DB_CONFIG["database"],
        )

        engine = create_engine(url)

        customers = pd.read_sql(
            "SELECT * FROM customers",
            engine
        )

        logger.info("Customer data extracted successfully.")

        return customers

    except Exception as e:
        logger.error(f"Database extraction failed: {e}")
        raise
