import pandas as pd
import sqlite3

conn=sqlite3.connect("products.db")
df=pd.read_sql_query("SELECT  * FROM products", conn)
conn.close()

for i, col in enumerate(df.columns):
    print(f"{i}: '{col}'")

df.columns = df.columns.str.strip().str.lower()
print("Column names in the table: ")
print(df.columns.tolist())


df['inventory value'] = df['unit cost'] * df['current stock']

df['low stock flag'] = df['current stock'] <= df['reorder point']

print(df[['Product Name', 'Unit Cost', 'Current Stock', 'Reorder Point', 'Inventory Value', 'Low Stock Flag']])
