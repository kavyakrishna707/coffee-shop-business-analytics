
from pathlib import Path
import pandas as pd

# ==========================================
# STEP 1: SET UP PROJECT FOLDERS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
CLEAN_DIR = BASE_DIR / "data" / "cleaned"
REPORT_DIR = BASE_DIR / "reports"

CLEAN_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# STEP 2: LOAD DATASETS
# ==========================================

sales_file = CLEAN_DIR / "sales_cleaned.csv"
customers_file = RAW_DIR / "customers.csv"
inventory_file = RAW_DIR / "inventory.csv"

sales = pd.read_csv(sales_file)
customers = pd.read_csv(customers_file)
inventory = pd.read_csv(inventory_file)

print("=" * 50)
print("COFFEE SHOP BUSINESS ANALYTICS")
print("=" * 50)

# ==========================================
# STEP 3: CLEAN CUSTOMER DATA
# ==========================================

customers = customers.drop_duplicates().copy()

for column in customers.select_dtypes(include="str").columns:
    customers[column] = customers[column].apply(
        lambda value: value.strip() if isinstance(value, str) else value
    )

customers.to_csv(
    CLEAN_DIR / "customers_cleaned.csv", index=False
)

print("\nCUSTOMER DATA")
print("Total customer records:", len(customers))
print("Missing values:")
print(customers.isnull().sum())

# ==========================================
# STEP 4: CLEAN INVENTORY DATA
# ==========================================

inventory = inventory.drop_duplicates().copy()

for column in inventory.select_dtypes(include="str").columns:
    inventory[column] = inventory[column].apply(
        lambda value: value.strip() if isinstance(value, str) else value
    )

inventory.to_csv(
    CLEAN_DIR / "inventory_cleaned.csv", index=False
)

print("\nINVENTORY DATA")
print("Total inventory products:", len(inventory))
print("Missing values:")
print(inventory.isnull().sum())

# ==========================================
# STEP 5: CLEAN SALES DATA
# ==========================================

sales = sales.drop_duplicates().copy()

# Remove extra spaces from text fields
for column in sales.select_dtypes(include="str").columns:
    sales[column] = sales[column].apply(
        lambda value: value.strip() if isinstance(value, str) else value
    )

# Convert numeric columns
for column in ["Quantity", "UnitPrice", "UnitCost"]:
    sales[column] = pd.to_numeric(
        sales[column], errors="coerce"
    )

# Convert dates
sales["Date"] = pd.to_datetime(
    sales["Date"], errors="coerce", dayfirst=True
)

# Remove records with missing essential sales information
sales = sales.dropna(
    subset=["Date", "Product", "Quantity", "UnitPrice", "UnitCost"]
)

# Keep valid positive quantities and non-negative prices/costs
sales = sales[
    (sales["Quantity"] > 0)
    & (sales["UnitPrice"] >= 0)
    & (sales["UnitCost"] >= 0)
].copy()

# ==========================================
# STEP 6: CALCULATE REVENUE, COST AND PROFIT
# ==========================================

sales["SalesAmount"] = sales["Quantity"] * sales["UnitPrice"]
sales["TotalCost"] = sales["Quantity"] * sales["UnitCost"]
sales["Profit"] = sales["SalesAmount"] - sales["TotalCost"]

# Save processed sales data
sales.to_csv(
    CLEAN_DIR / "sales_with_revenue.csv", index=False
)

# ==========================================
# STEP 7: OVERALL BUSINESS INSIGHTS
# ==========================================

total_revenue = sales["SalesAmount"].sum()
total_cost = sales["TotalCost"].sum()
total_profit = sales["Profit"].sum()
total_quantity = sales["Quantity"].sum()
total_orders = sales["OrderID"].nunique()

print("\n" + "=" * 50)
print("OVERALL BUSINESS PERFORMANCE")
print("=" * 50)

print("Valid sales records:", len(sales))
print("Unique orders:", total_orders)
print("Total quantity sold:", total_quantity)
print(f"Total revenue: {total_revenue:,.2f}")
print(f"Total cost: {total_cost:,.2f}")
print(f"Total profit: {total_profit:,.2f}")

if total_revenue != 0:
    profit_margin = (total_profit / total_revenue) * 100
    print(f"Profit margin: {profit_margin:.2f}%")

if total_orders > 0:
    average_order_value = total_revenue / total_orders
    print(f"Average order value: {average_order_value:,.2f}")

# ==========================================
# STEP 8: TOP 10 PRODUCTS BY REVENUE
# ==========================================

top_products = (
    sales.groupby("Product", as_index=False)
    .agg(
        Revenue=("SalesAmount", "sum"),
        QuantitySold=("Quantity", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS BY REVENUE")
print(top_products.to_string(index=False))

top_products.to_csv(
    REPORT_DIR / "top_products.csv", index=False
)

# ==========================================
# STEP 9: SALES BY CATEGORY
# ==========================================

category_sales = (
    sales.groupby("Category", as_index=False)
    .agg(
        Revenue=("SalesAmount", "sum"),
        Profit=("Profit", "sum"),
        QuantitySold=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

print("\nSALES PERFORMANCE BY CATEGORY")
print(category_sales.to_string(index=False))

category_sales.to_csv(
    REPORT_DIR / "category_sales.csv", index=False
)

# ==========================================
# STEP 10: MONTHLY SALES
# ==========================================

sales["Month"] = sales["Date"].dt.to_period("M").astype(str)

monthly_sales = (
    sales.groupby("Month", as_index=False)
    .agg(
        Revenue=("SalesAmount", "sum"),
        Profit=("Profit", "sum"),
        QuantitySold=("Quantity", "sum")
    )
    .sort_values("Month")
)

print("\nMONTHLY SALES PERFORMANCE")
print(monthly_sales.to_string(index=False))

monthly_sales.to_csv(
    REPORT_DIR / "monthly_sales.csv", index=False
)

# ==========================================
# STEP 11: SAVE FINAL CLEANED CUSTOMER DATA
# ==========================================

print("\n" + "=" * 50)
print("ANALYSIS COMPLETED")
print("=" * 50)

print("Cleaned customer file:",
      CLEAN_DIR / "customers_cleaned.csv")
print("Cleaned inventory file:",
      CLEAN_DIR / "inventory_cleaned.csv")
print("Processed sales file:",
      CLEAN_DIR / "sales_with_revenue.csv")
print("Reports folder:", REPORT_DIR)
