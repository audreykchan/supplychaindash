import pandas as pd
import sqlite3

conn=sqlite3.connect("products.db")
df=pd.read_sql_query("SELECT * FROM products", conn)
conn.close()

df.columns = df.columns.str.strip().str.lower()

search_term = input("Enter part of a product name to search for (or press Enter to skip): ").lower()

if search_term:
    df = df[df['product name'].str.lower().str.contains(search_term)]

categories = sorted(df['category'].unique())
print("\nAvailable categories:")
for i, cat in enumerate(categories):
    print(f"{i + 1}. {cat}")

category_input = input("\nEnter a category name to filter (or press Enter to skip): ").strip()

if category_input:
    df = df[df['category'].str.lower() == category_input.lower()]

print("\nFiltered Inventory:")
print(df[['product name', 'category', 'unit cost', 'current stock', 'reorder point']])