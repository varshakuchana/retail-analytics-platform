import requests
import pandas as pd

url = "https://dummyjson.com/products?limit=100"

response = requests.get(url)

data = response.json()["products"]

products = []

for item in data:
    products.append({
        "product_id": item["id"],
        "title": item["title"],
        "category": item["category"],
        "brand": item.get("brand", "Unknown"),
        "price": item["price"],
        "rating": item["rating"],
        "stock": item["stock"]
    })

df = pd.DataFrame(products)

df.to_csv("data/products.csv", index=False)

print(df.head())
print("\nProducts saved successfully")
