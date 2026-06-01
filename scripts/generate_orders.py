import pandas as pd
import random
from datetime import datetime, timedelta

products = pd.read_csv("data/products.csv")

customers = []
states = ["MO", "IL", "TX", "CA", "NY", "FL", "GA", "WA"]
segments = ["New", "Returning", "VIP"]

for i in range(1, 501):
    customers.append({
        "customer_id": i,
        "customer_name": f"Customer {i}",
        "city": f"City {random.randint(1, 50)}",
        "state": random.choice(states),
        "segment": random.choice(segments)
    })

customers_df = pd.DataFrame(customers)

orders = []
order_items = []

start_date = datetime.today() - timedelta(days=180)
order_id = 1
order_item_id = 1

for day in range(180):
    current_date = start_date + timedelta(days=day)
    number_of_orders = random.randint(20, 80)

    for _ in range(number_of_orders):
        customer = random.choice(customers)
        num_items = random.randint(1, 4)
        selected_products = products.sample(num_items)

        total_amount = 0

        for _, product in selected_products.iterrows():
            quantity = random.randint(1, 3)
            unit_price = product["price"]
            total_price = quantity * unit_price
            total_amount += total_price

            order_items.append({
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": int(product["product_id"]),
                "quantity": quantity,
                "unit_price": round(unit_price, 2),
                "total_price": round(total_price, 2)
            })

            order_item_id += 1

        orders.append({
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "order_date": current_date.date(),
            "total_amount": round(total_amount, 2),
            "order_status": "Completed"
        })

        order_id += 1

orders_df = pd.DataFrame(orders)
order_items_df = pd.DataFrame(order_items)

customers_df.to_csv("data/customers.csv", index=False)
orders_df.to_csv("data/orders.csv", index=False)
order_items_df.to_csv("data/order_items.csv", index=False)

print("Generated files:")
print("data/customers.csv")
print("data/orders.csv")
print("data/order_items.csv")

print("\nCustomers:", len(customers_df))
print("Orders:", len(orders_df))
print("Order items:", len(order_items_df))

