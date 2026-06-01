import pandas as pd
from sqlalchemy import create_engine

username = "postgres"
password = "postgres123"
host = "localhost"
port = "5432"
database = "retail_analytics"

engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)

tables = {
    "customers": "data/customers.csv",
    "orders": "data/orders.csv",
    "order_items": "data/order_items.csv"
}

for table_name, file_path in tables.items():
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name}: {len(df)} rows loaded")

