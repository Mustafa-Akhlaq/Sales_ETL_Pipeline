from extract import extract_csv, extract_customers
from transform import transform_data
from load import load_data
from logger import logger

try:
    sales = extract_csv()
    customers = extract_customers()

    final_df = transform_data(sales, customers)

    load_data(final_df)

    logger.info("ETL Pipeline Completed Successfully")

except Exception as e:
    logger.error(f"ETL Pipeline Failed: {e}")
    print("ETL Pipeline Failed. Check etl.log for details.")


print("\n" + "=" * 50)
print("ETL PIPELINE SUMMARY")
print("=" * 50)

print(f"Sales Records: {len(sales)}")
print(f"Customer Records: {len(customers)}")
print(f"Final Records Loaded: {len(final_df)}")

print("\nStatus: SUCCESS")
