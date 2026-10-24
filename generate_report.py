
from pathlib import Path
import pandas as pd

# ==========================================
# 1. PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "cleaned"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

sales_file = DATA_DIR / "sales_with_revenue.csv"
customers_file = DATA_DIR / "customers_cleaned.csv"
inventory_file = DATA_DIR / "inventory_cleaned.csv"

# ==========================================
# 2. LOAD DATA
# ==========================================

sales = pd.read_csv(sales_file)
customers = pd.read_csv(customers_file)
inventory = pd.read_csv(inventory_file)

sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")
sales["SalesAmount"] = pd.to_numeric(
    sales["SalesAmount"], errors="coerce"
)
sales["Profit"] = pd.to_numeric(sales["Profit"], errors="coerce")
sales["Quantity"] = pd.to_numeric(sales["Quantity"], errors="coerce")

sales = sales.dropna(
    subset=["Date", "Product", "SalesAmount", "Profit"]
)

# ==========================================
# 3. CALCULATE KEY PERFORMANCE INDICATORS
# ==========================================

revenue = sales["SalesAmount"].sum()
profit = sales["Profit"].sum()
quantity = sales["Quantity"].sum()
orders = sales["OrderID"].nunique()

profit_margin = profit / revenue * 100 if revenue else 0
average_order_value = revenue / orders if orders else 0

top_products = (
    sales.groupby("Product")
    .agg(
        Revenue=("SalesAmount", "sum"),
        Profit=("Profit", "sum"),
        QuantitySold=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
    .head(10)
)

category_sales = (
    sales.groupby("Category")
    .agg(
        Revenue=("SalesAmount", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

monthly_sales = (
    sales.assign(Month=sales["Date"].dt.to_period("M").astype(str))
    .groupby("Month")["SalesAmount"]
    .sum()
    .sort_index()
)

# ==========================================
# 4. PREPARE BUSINESS FINDINGS
# ==========================================

best_product = top_products.index[0] if not top_products.empty else "N/A"
best_category = (
    category_sales["Revenue"].idxmax()
    if not category_sales.empty else "N/A"
)
most_profitable_category = (
    category_sales["Profit"].idxmax()
    if not category_sales.empty else "N/A"
)

if not monthly_sales.empty:
    best_month = monthly_sales.idxmax()
    best_month_revenue = monthly_sales.max()
else:
    best_month = "N/A"
    best_month_revenue = 0

# ==========================================
# 5. CREATE THE BUSINESS REPORT
# ==========================================

report = f"""# Coffee Shop Business Analytics Capstone Project

## 1. Introduction

This project analyzes coffee shop sales, customer information, and inventory
data using Python, pandas, data visualization, and Microsoft Power BI.

The objective is to understand sales performance, product popularity,
profitability, and opportunities to improve business decisions.

## 2. Project Objectives

- Analyze overall revenue and profit.
- Identify top-performing products.
- Compare sales and profit across product categories.
- Examine monthly sales trends.
- Review customer and inventory data.
- Present business performance through an interactive Power BI dashboard.

## 3. Tools and Technologies

- Python
- pandas
- Matplotlib
- CSV datasets
- Microsoft Power BI Desktop
- Visual Studio Code

MySQL was not used in this implementation.

## 4. Dataset Description

The project uses three datasets:

1. Sales dataset: order ID, date, time, product, category, quantity,
   unit price, unit cost, and customer ID.
2. Customer dataset: customer details, joining date, visit count,
   spending, and last visit date.
3. Inventory dataset: product, available stock, reorder level, unit cost,
   supplier, and wasted units.

The project datasets are synthetically generated for demonstration and
learning purposes.

## 5. Data Preparation

The data preparation process included:

- Loading CSV files using pandas.
- Removing duplicate sales records.
- Trimming extra spaces from text fields.
- Converting date and numeric fields to suitable data types.
- Removing sales records missing essential fields.
- Excluding non-positive quantities and negative prices or costs.
- Saving cleaned and processed datasets for further analysis.

## 6. Key Performance Indicators

| Metric | Result |
|---|---:|
| Valid sales records | {len(sales):,} |
| Unique orders | {orders:,} |
| Total quantity sold | {quantity:,.0f} |
| Total revenue | {revenue:,.2f} |
| Total cost | {(revenue - profit):,.2f} |
| Total profit | {profit:,.2f} |
| Profit margin | {profit_margin:.2f}% |
| Average order value | {average_order_value:,.2f} |
| Customer records | {len(customers):,} |
| Inventory product records | {len(inventory):,} |

Revenue is calculated as quantity multiplied by unit price.
Profit is calculated as revenue minus the total cost of goods sold.

## 7. Product Performance

The top products are ranked by total revenue.

{top_products.reset_index().to_markdown(index=False)}

The highest-revenue product in this analysis is **{best_product}**.
Management could review its availability, demand, and contribution to profit
before making inventory or promotional decisions.

## 8. Category Performance

{category_sales.reset_index().to_markdown(index=False)}

The highest-revenue category is **{best_category}**.
The highest-profit category is **{most_profitable_category}**.

Revenue and profit are different measures. A category with the highest revenue
does not necessarily have the highest profit.

## 9. Monthly Sales Analysis

{monthly_sales.to_frame("Revenue").reset_index().to_markdown(index=False)}

The highest-revenue month in the dataset is **{best_month}**, with revenue of
**{best_month_revenue:,.2f}**.

Monthly trends can help the business investigate periods of high and low demand
and plan staffing, inventory, and promotions.

## 10. Power BI Dashboard

The Power BI dashboard contains:

- Total Revenue card.
- Total Profit card.
- Top 10 Products by Revenue bar chart.
- Monthly Sales Trend line chart.
- Profit by Category column chart.
- Category and date slicers, where configured.

The dashboard allows users to explore performance and filter results
interactively.

## 11. Business Recommendations

1. **Product management:** Monitor demand for the top-revenue products and
   ensure that popular items remain available.
2. **Profitability:** Compare revenue, cost, and profit before choosing products
   for promotions.
3. **Inventory planning:** Compare available stock with reorder levels and
   investigate wasted units to identify possible improvements.
4. **Sales planning:** Use monthly sales trends to guide staffing, purchasing,
   and promotional planning.
5. **Customer retention:** Examine visit frequency and spending to identify
   opportunities for loyalty programs.
6. **Ongoing monitoring:** Refresh the datasets and review the Power BI
   dashboard regularly.

These recommendations should be validated against actual business conditions
before being implemented.

## 12. Limitations

The datasets are synthetically generated. Therefore, the results demonstrate
an analytics workflow and should not be treated as evidence of the performance
of a real coffee shop.

The analysis also depends on the completeness and quality of the generated
data. Further validation would be required before operational use.

## 13. Conclusion

This project demonstrates how Python can be used to prepare datasets, calculate
business performance indicators, identify product and category trends, and
create visualizations. Microsoft Power BI presents these findings through an
interactive dashboard to support data-informed business decisions.

## 14. Project Deliverables

- Generated CSV datasets.
- Cleaned sales, customer, and inventory data.
- Python analysis and visualization scripts.
- Business insight CSV files and charts.
- Power BI dashboard.
- Business analysis report.
"""

report_file = REPORT_DIR / "business_report.md"
report_file.write_text(report, encoding="utf-8")

print("Business report generated successfully!")
print("Report saved to:", report_file)
print("\nTop product:", best_product)
print("Top revenue category:", best_category)
print("Most profitable category:", most_profitable_category)
print("Best month:", best_month)
