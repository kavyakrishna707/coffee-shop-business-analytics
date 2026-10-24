# ☕ Coffee Shop Business Analytics

**A Data Analytics Capstone Project using Python, Pandas, Matplotlib, and Power BI**

## 📌 Project Overview

Coffee Shop Business Analytics is a data analytics project designed to analyze coffee shop business performance using sales, customer, and inventory data.

The project transforms raw CSV datasets into meaningful business insights through data cleaning, exploratory data analysis, visualization, and an interactive Power BI dashboard.

It helps understand revenue, profitability, product performance, category-wise sales, and monthly sales trends to support data-driven business decisions.

## 🎯 Objectives

- Analyze coffee shop sales and revenue.
- Calculate total profit and identify profitable products.
- Understand product and category performance.
- Explore monthly sales trends.
- Analyze customer and inventory information.
- Create visualizations and an interactive Power BI dashboard.
- Generate business insights and recommendations.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and automation |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| CSV | Dataset storage |
| Power BI | Interactive dashboard and reporting |
| VS Code | Development environment |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
Coffee-Shop-Business-Analytics/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── powerbi/
│   └── Coffee_Shop_Analytics.pbix
│
├── reports/
│   └── business_report.md
│
├── generate_dataset.py
├── business_insights.py
├── analyze_data.py
├── visualize_data.py
├── generate_report.py
│
├── requirements.txt
└── README.md
```

*Note: The folder and file names shown above should match your actual project files.*

## 📊 Dataset Description

The project uses CSV datasets for three main business areas:

- **Sales Data:** Order information, dates, products, categories, quantities, prices, costs, revenue, and profit.
- **Customer Data:** Customer-related information for analyzing customer records.
- **Inventory Data:** Inventory-related information for examining stock levels.

The datasets are generated locally using Python for this project.

## 📈 Power BI Dashboard

The dashboard presents key performance indicators and visualizations, including:

- **Total Revenue**
- **Total Profit**
- **Top 10 Products**
- **Monthly Sales Trend**
- **Profit by Category**
- **Category-based filtering**

These visualizations help identify sales patterns and compare product and category performance.

## 🔍 Key Analysis

The project focuses on:

1. Data cleaning and preprocessing.
2. Exploratory data analysis.
3. Revenue and profit calculations.
4. Product performance analysis.
5. Category-wise business analysis.
6. Monthly trend analysis.
7. Business insight generation.
8. Interactive dashboard development.

## 💡 Business Value

The insights from this project can help a coffee shop:

- Identify high-performing products.
- Understand which categories contribute more to revenue and profit.
- Monitor sales trends over time.
- Make informed inventory decisions.
- Improve business planning using data-driven insights.

## ⚙️ Installation and Setup

### Prerequisites

- Python installed on your computer
- Visual Studio Code
- Power BI Desktop for opening the dashboard

### 1. Clone the Repository

```bash
git clone https://github.com/kavyakrishna707/coffee-shop-business-analytics.git
```

### 2. Open the Project Folder

```bash
cd coffee-shop-business-analytics
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment on Windows

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Generate the Datasets

```bash
python generate_dataset.py
```

### 7. Run the Analysis

```bash
python business_insights.py
python analyze_data.py
python visualize_data.py
```

### 8. Generate the Business Report

```bash
python generate_report.py
```

**Note:** Run the scripts in the order required by your implementation. If the CSV datasets are already available, you may not need to generate them again. Some scripts may require the cleaned datasets to be created first.

