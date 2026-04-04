import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_df = pd.read_excel("Wholesale_customers_data.xlsx")

channel_sum = [0, 0]
region_sum = [0, 0, 0]

# Calculate totals
for i in range(len(data_df)):
    total_products = data_df.iloc[i, 2:8].astype(float).sum()
    channel_sum[data_df.iloc[i, 0] - 1] += total_products
    region_sum[data_df.iloc[i, 1] - 1] += total_products

# Labels
x1 = ["Gujarat","West Bengal","Other"]
x2 = ["Hotel","Retail"]

# Create one figure with 2 subplots
plt.figure(figsize=(10,5))

# Plot 1: Region
plt.subplot(1,2,1)
plt.bar(x1, region_sum, color=['blue','green','orange'])
plt.xlabel("Regions")
plt.ylabel("Total Products")
plt.title("Region-wise Spending")

# Plot 2: Channel
plt.subplot(1,2,2)
plt.bar(x2, channel_sum, color=['red','purple'])
plt.xlabel("Channels")
plt.ylabel("Total Products")
plt.title("Channel-wise Spending")

plt.tight_layout()
plt.show()