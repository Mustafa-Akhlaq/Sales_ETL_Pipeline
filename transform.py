import pandas as pd
from logger import logger


def transform_data(sales, customers):
    try:
        # Convert date columns

        sales['order_date'] = pd.to_datetime(sales['order_date'])

        customers['signup_date'] = pd.to_datetime(customers['signup_date'])

        # Merge sales with customer data

        final_df = pd.merge(
            sales,
            customers,
            on="customer_id",
            how="left"
        )

        # FEATURE ENGINEERING----------------------------------------------------

        # Calculate Total Sale
        final_df['total_sale'] = (
            final_df['unit_price'] * final_df['quantity']).round(2)

        # Extract Month
        final_df['order_month'] = final_df['order_date'].dt.month_name()

        # Extract Year
        final_df['order_year'] = final_df['order_date'].dt.year

        # Customer Tenure
        final_df['customer_tenure_days'] = (
            final_df['order_date'] - final_df['signup_date']
        ).dt.days

        logger.info("Data Transformed Successfully.")

        return final_df

    except Exception as e:
        logger.error(f"tranformation Failed: {e}")
        raise
