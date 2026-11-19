import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. CREATE SALES DATA - Simulate a retail company in Zimbabwe
np.random.seed(42)
n = 5000
products = ['Milk', 'Bread', 'Rice', 'Cooking Oil', 'Sugar', 'Soap']
regions = ['Harare', 'Bulawayo', 'Mutare', 'Gweru', 'Masvingo']
branches = ['Branch A', 'Branch B', 'Branch C']

data = {
    'date': pd.date_range('2024-01-01', periods=n, freq='D').tolist()[:n],
    'product': np.random.choice(products, n),
    'region': np.random.choice(regions, n, p=[0.4, 0.2, 0.15, 0.15, 0.1]),
    'branch': np.random.choice(branches, n),
    'quantity': np.random.randint(1, 20, n),
    'unit_price': np.random.choice([2.5, 1.5, 8, 5, 3, 2], n)
}
df = pd.DataFrame(data)
df['revenue'] = df['quantity'] * df['unit_price']
df['month'] = df['date'].dt.to_period('M')

print("=== SALES DASHBOARD KPIs ===")
print(f"Total Revenue: ${df['revenue'].sum():,.2f}")
print(f"Total Transactions: {len(df)}")
print(f"Average Basket: ${df['revenue'].mean():.2f}")
print(f"Best Product: {df.groupby('product')['revenue'].sum().idxmax()}")
print(f"Best Region: {df.groupby('region')['revenue'].sum().idxmax()}")

# 2. ANALYSIS FOR DASHBOARD
print("\n--- Revenue by Month ---")
print(df.groupby('month')['revenue'].sum())

print("\n--- Top 5 Products ---")
print(df.groupby('product')['revenue'].sum().sort_values(ascending=False))

print("\n--- Revenue by Region ---")
print(df.groupby('region')['revenue'].sum().sort_values(ascending=False))

print("\n--- Revenue by Branch ---")
print(df.groupby('branch')['revenue'].sum())

# 3. CREATE CHARTS - These are your dashboard visuals
plt.figure(figsize=(10, 5))
df.groupby('month')['revenue'].sum().plot(kind='bar', color='skyblue')
plt.title('Monthly Revenue')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.savefig('monthly_revenue.png')
print("\nSaved: monthly_revenue.png")

plt.figure(figsize=(10, 5))
df.groupby('product')['revenue'].sum().sort_values().plot(kind='barh', color='green')
plt.title('Revenue by Product')
plt.xlabel('Revenue ($)')
plt.tight_layout()
plt.savefig('revenue_by_product.png')
print("Saved: revenue_by_product.png")

plt.figure(figsize=(10, 5))
df.groupby('region')['revenue'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Revenue Share by Region')
plt.ylabel('')
plt.tight_layout()
plt.savefig('revenue_by_region.png')
print("Saved: revenue_by_region.png")

# Save clean data for Power BI / Excel
df.to_csv('sales_data.csv', index=False)
print("\nSaved: sales_data.csv - Open this in Power BI or Excel to build dashboard")
