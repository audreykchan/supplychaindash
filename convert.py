import pandas as pd
import sqlite3

df = pd.read_csv("products_export.csv", delimiter="|")

print("Preview after reading CSV:")
print(df.head())
print("\nColumns detected:")
print(df.columns.tolist())

column_names = [
    "Product ID",
    "Product Name",
    "Category",
    "Unit Cost",
    "Current Stock",
    "Reorder Point"
]

df = pd.read_csv("products_export.csv", delimiter="|", header=None, names=column_names)

print("Preview of clean data:")
print(df.head())
print("\nColumns detected:")
print(df.columns.tolist())

conn = sqlite3.connect("products.db")
df.to_sql("products", conn, if_exists="replace", index=False)
conn.close()
