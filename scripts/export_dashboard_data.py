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

query = """
SELECT
o.order_date,
c.state,
c.segment,
p.title,
oi.quantity,
oi.total_price
FROM order_items oi
JOIN orders o
ON oi.order_id=o.order_id
JOIN products p
ON oi.product_id=p.product_id
JOIN customers c
ON o.customer_id=c.customer_id
"""

df = pd.read_sql(query, engine)

df.to_csv(
    "data/dashboard_data.csv",
    index=False
)

print("Dashboard data exported")
print(df.head())
