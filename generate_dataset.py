
import random
from pathlib import Path
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Make the generated data reproducible
random.seed(42)
np.random.seed(42)

# Project folders
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------
# 1. PRODUCT INFORMATION
# -------------------------------

products = [
    {"Product": "Cappuccino", "Category": "Coffee",
     "UnitPrice": 150, "UnitCost": 65},
    {"Product": "Latte", "Category": "Coffee",
     "UnitPrice": 170, "UnitCost": 75},
    {"Product": "Espresso", "Category": "Coffee",
     "UnitPrice": 100, "UnitCost": 35},
    {"Product": "Americano", "Category": "Coffee",
     "UnitPrice": 120, "UnitCost": 40},
    {"Product": "Green Tea", "Category": "Tea",
     "UnitPrice": 90, "UnitCost": 25},
    {"Product": "Black Tea", "Category": "Tea",
     "UnitPrice": 60, "UnitCost": 15},
    {"Product": "Croissant", "Category": "Bakery",
     "UnitPrice": 90, "UnitCost": 40},
    {"Product": "Blueberry Muffin", "Category": "Bakery",
     "UnitPrice": 110, "UnitCost": 45},
    {"Product": "Chocolate Cake", "Category": "Dessert",
     "UnitPrice": 140, "UnitCost": 60},
    {"Product": "Sandwich", "Category": "Food",
     "UnitPrice": 180, "UnitCost": 90},
]

product_names = [p["Product"] for p in products]
product_lookup = {p["Product"]: p for p in products}

# -------------------------------
# 2. GENERATE CUSTOMERS
# -------------------------------

first_names = [
    "Anu", "Rahul", "Meera", "Arjun", "Diya",
    "Akhil", "Neha", "Riya", "Vishnu", "Asha",
    "Nikhil", "Sneha", "Kiran", "Amal", "Sara"
]

customers = []

for i in range(1, 301):
    join_date = datetime(2025, 1, 1) + timedelta(
        days=random.randint(0, 364)
    )

    customers.append({
        "CustomerID": f"C{i:03d}",
        "CustomerName": random.choice(first_names)
                        + f" {i}",
        "JoinDate": join_date.strftime("%Y-%m-%d"),
        "VisitCount": 0,
        "TotalSpending": 0.0,
        "LastVisitDate": ""
    })

customers_df = pd.DataFrame(customers)

# -------------------------------
# 3. GENERATE SALES
# -------------------------------

start_date = datetime(2025, 1, 1)
sales_rows = []

# Products have different selection weights
weights = [18, 15, 10, 12, 8, 7, 9, 7, 6, 8]

for i in range(1, 5001):
    customer = random.choice(customers)
    product = random.choices(products, weights=weights, k=1)[0]

    # Random date across 2025 and early 2026
    sale_date = start_date + timedelta(
        days=random.randint(0, 454)
    )

    # Coffee shop sales are more common in the morning
    hour = random.choices(
        range(7, 22),
        weights=[5, 9, 10, 8, 5, 4, 4, 4, 5, 6, 8, 9, 7, 5, 3],
        k=1
    )[0]

    minute = random.choice([0, 15, 30, 45])
    sale_time = f"{hour:02d}:{minute:02d}:00"

    quantity = random.choices(
        [1, 2, 3, 4],
        weights=[65, 25, 8, 2],
        k=1
    )[0]

    sales_rows.append({
        "OrderID": f"O{i:05d}",
        "Date": sale_date.strftime("%Y-%m-%d"),
        "Time": sale_time,
        "Product": product["Product"],
        "Category": product["Category"],
        "Quantity": quantity,
        "UnitPrice": product["UnitPrice"],
        "UnitCost": product["UnitCost"],
        "CustomerID": customer["CustomerID"]
    })

sales_df = pd.DataFrame(sales_rows)

# Calculate customer summaries from the sales records
customer_spending = (
    sales_df.assign(
        Amount=sales_df["Quantity"] * sales_df["UnitPrice"]
    )
    .groupby("CustomerID")
    .agg(
        VisitCount=("OrderID", "count"),
        TotalSpending=("Amount", "sum"),
        LastVisitDate=("Date", "max")
    )
)

customers_df = customers_df.drop(
    columns=["VisitCount", "TotalSpending", "LastVisitDate"]
).join(customer_spending, on="CustomerID")

customers_df["VisitCount"] = (
    customers_df["VisitCount"].fillna(0).astype(int)
)
customers_df["TotalSpending"] = (
    customers_df["TotalSpending"].fillna(0).round(2)
)
customers_df["LastVisitDate"] = (
    customers_df["LastVisitDate"].fillna("")
)

# -------------------------------
# 4. GENERATE INVENTORY
# -------------------------------

suppliers = [
    "Supplier A", "Supplier B", "Supplier C",
    "Supplier D", "Supplier E"
]

inventory_rows = []

for product in products:
    stock = random.randint(5, 100)
    reorder_level = random.randint(10, 30)

    inventory_rows.append({
        "Product": product["Product"],
        "StockAvailable": stock,
        "ReorderLevel": reorder_level,
        "UnitCost": product["UnitCost"],
        "Supplier": random.choice(suppliers),
        "WastedUnits": random.randint(0, 12)
    })

inventory_df = pd.DataFrame(inventory_rows)

# -------------------------------
# 5. INTRODUCE MESSY DATA
# -------------------------------
# These issues are intentional for cleaning practice.

# Add duplicate sales records
sales_df = pd.concat(
    [sales_df, sales_df.iloc[[10, 25]]],
    ignore_index=True
)

# Introduce inconsistent product spelling
sales_df.loc[5, "Product"] = "cappuccino"
sales_df.loc[15, "Product"] = "Latte "

# Introduce missing values
sales_df.loc[20, "UnitPrice"] = np.nan
sales_df.loc[30, "Quantity"] = np.nan

# Introduce a date in a different format
sales_df.loc[40, "Date"] = pd.to_datetime(
    sales_df.loc[40, "Date"]
).strftime("%d/%m/%Y")

# Introduce a missing customer name
customers_df.loc[5, "CustomerName"] = np.nan

# Introduce a spelling inconsistency in supplier names
inventory_df.loc[0, "Supplier"] = "supplier a"

# -------------------------------
# 6. SAVE THE CSV FILES
# -------------------------------

sales_df.to_csv(
    RAW_DIR / "sales.csv", index=False
)

customers_df.to_csv(
    RAW_DIR / "customers.csv", index=False
)

inventory_df.to_csv(
    RAW_DIR / "inventory.csv", index=False
)

print("Dataset generation completed!")
print(f"Sales records: {len(sales_df)}")
print(f"Customer records: {len(customers_df)}")
print(f"Inventory records: {len(inventory_df)}")
print(f"Files saved in: {RAW_DIR}")
