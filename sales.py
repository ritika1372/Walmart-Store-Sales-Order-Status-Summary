# Grouping by Store and Order Status
summary = df.groupby(['Store', 'Order_Status'])['Weekly_Sales'].sum().reset_index()

# Sort and display
print(summary.sort_values(by='Weekly_Sales', ascending=False))
