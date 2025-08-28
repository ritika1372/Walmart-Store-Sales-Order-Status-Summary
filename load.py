import pandas as pd

# Load the CSV
df = pd.read_csv("Walmart_Store_sales.csv")

# Quick look
print(df.head())
print(df.info())
