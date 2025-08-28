import seaborn as sns
import matplotlib.pyplot as plt

# Heatmap of Sales by Store and Order Status
plt.figure(figsize=(12, 6))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("📦 Walmart Order Status Summary by Store")
plt.ylabel("Store")
plt.xlabel("Order Status")
plt.tight_layout()
plt.show()
