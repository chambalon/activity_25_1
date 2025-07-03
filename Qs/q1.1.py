import csv
import pandas as pd

try:
  df = pd.read_csv('transaction.csv')
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit()
print(df)

df.columns = df.columns.str.strip()

df_filtered = df.dropna()

#df_filtered = df[df['TotalSalesAmount'] > 0]

df_aggregated = df_filtered.groupby('CustomerID')['TotalSales'].aggregate('sum')

print(df_aggregated)