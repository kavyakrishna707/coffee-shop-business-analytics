# Coffee Shop Business Analytics Capstone Project

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
| Valid sales records | 1,978 |
| Unique orders | 1,978 |
| Total quantity sold | 2,901 |
| Total revenue | 365,140.00 |
| Total cost | 149,100.00 |
| Total profit | 216,040.00 |
| Profit margin | 59.17% |
| Average order value | 184.60 |
| Customer records | 300 |
| Inventory product records | 10 |

Revenue is calculated as quantity multiplied by unit price.
Profit is calculated as revenue minus the total cost of goods sold.

## 7. Product Performance

The top products are ranked by total revenue.

| Product          |   Revenue |   Profit |   QuantitySold |
|:-----------------|----------:|---------:|---------------:|
| Cappuccino       |     76500 |    43350 |            510 |
| Latte            |     73390 |    41025 |            432 |
| Sandwich         |     40860 |    20430 |            227 |
| Americano        |     40560 |    27040 |            338 |
| Espresso         |     29700 |    19305 |            297 |
| Croissant        |     27810 |    15450 |            309 |
| Chocolate Cake   |     22960 |    13120 |            164 |
| Green Tea        |     21060 |    15210 |            234 |
| Blueberry Muffin |     19580 |    11570 |            178 |
| Black Tea        |     12720 |     9540 |            212 |

The highest-revenue product in this analysis is **Cappuccino**.
Management could review its availability, demand, and contribution to profit
before making inventory or promotional decisions.

## 8. Category Performance

| Category   |   Revenue |   Profit |
|:-----------|----------:|---------:|
| Coffee     |    220150 |   130720 |
| Bakery     |     47390 |    27020 |
| Food       |     40860 |    20430 |
| Tea        |     33780 |    24750 |
| Dessert    |     22960 |    13120 |

The highest-revenue category is **Coffee**.
The highest-profit category is **Coffee**.

Revenue and profit are different measures. A category with the highest revenue
does not necessarily have the highest profit.

## 9. Monthly Sales Analysis

| Month   |   Revenue |
|:--------|----------:|
| 2025-01 |     25860 |
| 2025-02 |     26590 |
| 2025-03 |     22500 |
| 2025-04 |     24790 |
| 2025-05 |     22260 |
| 2025-06 |     25110 |
| 2025-07 |     23640 |
| 2025-08 |     25150 |
| 2025-09 |     22590 |
| 2025-10 |     24930 |
| 2025-11 |     27810 |
| 2025-12 |     23460 |
| 2026-01 |     24820 |
| 2026-02 |     25900 |
| 2026-03 |     19730 |

The highest-revenue month in the dataset is **2025-11**, with revenue of
**27,810.00**.

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
