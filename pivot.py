# Pivot Table: Stores as rows, Order_Status as columns
pivot = df.pivot_table(
    index='Store',
    columns='Order_Status',
    values='Weekly_Sales',
    aggfunc='sum',
    fill_value=0
)

print(pivot)
