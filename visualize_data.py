
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: SET UP FOLDERS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "cleaned" / "sales_with_revenue.csv"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# STEP 2: LOAD PROCESSED SALES DATA
# ==========================================

df = pd.read_csv(DATA_FILE)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("=" * 50)
print("COFFEE SHOP SALES VISUALIZATION")
print("=" * 50)

# ==========================================
# CHART 1: TOP 10 PRODUCTS BY REVENUE
# ==========================================

product_sales = (
    df.groupby("Product")["SalesAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(11, 6))
product_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Coffee Shop Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(
    REPORT_DIR / "top_products_chart.png",
    dpi=150,
    bbox_inches="tight"
)
plt.close()

print("Created: top_products_chart.png")

# ==========================================
# CHART 2: DAILY SALES TREND
# ==========================================

daily_sales = (
    df.dropna(subset=["Date"])
    .groupby("Date")["SalesAmount"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 6))
daily_sales.plot(kind="line", marker="o", markersize=3)

plt.title("Daily Coffee Shop Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    REPORT_DIR / "daily_sales_chart.png",
    dpi=150,
    bbox_inches="tight"
)
plt.close()

print("Created: daily_sales_chart.png")

# ==========================================
# CHART 3: PROFIT BY CATEGORY
# ==========================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
category_profit.plot(kind="bar")

plt.title("Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()

plt.savefig(
    REPORT_DIR / "category_profit_chart.png",
    dpi=150,
    bbox_inches="tight"
)
plt.close()

print("Created: category_profit_chart.png")

# ==========================================
# CHART 4: MONTHLY REVENUE
# ==========================================

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_revenue = (
    df.dropna(subset=["Date"])
    .groupby("Month")["SalesAmount"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(11, 6))
monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Coffee Shop Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    REPORT_DIR / "monthly_revenue_chart.png",
    dpi=150,
    bbox_inches="tight"
)
plt.close()

print("Created: monthly_revenue_chart.png")

# ==========================================
# COMPLETION
# ==========================================

print("\nAll visualization charts have been saved!")
print("Location:", REPORT_DIR)
