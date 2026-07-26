import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config import DB_CONFIG
from logger import logger
import os


def load_data(final_df):
    try:
        url = URL.create(
            drivername="postgresql+psycopg2",
            username=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            database=DB_CONFIG['database']
        )

        engine = create_engine(url)

        final_df.to_sql(
            name="sales_customer_fact",
            con=engine,
            if_exists="replace",
            index=False
        )

        # Create output folder if it doesn't exist
        os.makedirs("output", exist_ok=True)

        final_df.to_csv(
            "output/final_sales_data.csv",
            index=False
        )

        logger.info("Data Loaded Successfully")

    except Exception as e:
        logger.error(f"Loading failed: {e}")
        raise
