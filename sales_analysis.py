import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales_data.csv")

# Show first rows
print(data.head())

# Total sales by region
region_sales = data.groupby("Region")["Sales"].sum()
print(region_sales)

# Plot sales by region
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()
