
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Find the project folders
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
CLEAN_DIR = BASE_DIR / "data" / "cleaned"
REPORT_DIR = BASE_DIR / "reports"

CLEAN_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load the sales dataset
sales_file = RAW_DIR / "sales.csv"
df = pd.read_csv(sales_file)

print("\n========== ORIGINAL DATA ==========")
print("Number of rows:", len(df))
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst 5 records:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Clean text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].apply(
        lambda value: value.strip() if isinstance(value, str) else value
    )

# Convert common date columns to datetime
for column in df.columns:
    if "date" in column.lower():
        df[column] = pd.to_datetime(df[column], errors="coerce", dayfirst=True)

# Convert numeric-looking columns
for column in df.columns:
    if any(word in column.lower() for word in
           ["quantity", "price", "amount", "total", "sales", "discount"]):
        df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove rows that are completely empty
df = df.dropna(how="all")

# Save the cleaned dataset
clean_file = CLEAN_DIR / "sales_cleaned.csv"
df.to_csv(clean_file, index=False)

print("\n========== CLEANING RESULTS ==========")
print("Rows after cleaning:", len(df))
print("Duplicate rows removed.")
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nCleaned dataset saved to:", clean_file)

# Explore the numerical data
print("\n========== NUMERICAL SUMMARY ==========")
print(df.describe(include="all").transpose())

# Create a chart for the first suitable numeric column
numeric_columns = df.select_dtypes(include="number").columns.tolist()

if numeric_columns:
    column = numeric_columns[0]

    df[column].dropna().plot(
        kind="hist",
        bins=15,
        title=f"Distribution of {column}"
    )

    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()

    chart_file = REPORT_DIR / "sales_distribution.png"
    plt.savefig(chart_file)
    plt.show()

    print("\nChart saved to:", chart_file)
else:
    print("\nNo numeric columns were found for plotting.")
