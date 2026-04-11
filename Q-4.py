# import pandas as pd
# import matplotlib.pyplot as plt

# data_df = pd.read_excel("Wholesale_customers_data.xlsx")

# items = ['Fresh','Milk','Grocery','Frozen','Detergents_Paper','Delicassen']

# plt.figure(figsize=(10,6))
# plt.boxplot([data_df[col] for col in items], labels=items)

# plt.title("Outlier Detection using Box Plot")
# plt.xlabel("Product Variety")
# plt.ylabel("Spending")

# plt.xticks(rotation=30)
# plt.show()

import pandas as pd

data_df = pd.read_excel("Wholesale_customers_data.xlsx")

items = ['Fresh','Milk','Grocery','Frozen','Detergents_Paper','Delicassen']

for col in items:
    Q1 = data_df[col].quantile(0.25)
    Q3 = data_df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = data_df[(data_df[col] < lower) | (data_df[col] > upper)]

    print(col, "→", len(outliers), "outliers")