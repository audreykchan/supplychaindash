import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Load and clean
conn = sqlite3.connect("products.db")
df = pd.read_sql_query("SELECT * FROM products", conn)
conn.close()

df.columns = df.columns.str.strip().str.lower()

# Search bar on side
st.sidebar.header("Filter Inventory")
search_term = st.sidebar.text_input("Search by Product Name")

# Dropdown filter by category
category_options = ["All"] + sorted(df["category"].unique())
selected_category = st.sidebar.selectbox("Filter by Category", category_options)

# Apply filters
if search_term:
    df = df[df["product name"].str.lower().str.contains(search_term.lower())]

if selected_category != "All":
    df = df[df["category"] == selected_category]

st.subheader("Filtered Inventory")
st.dataframe(df)

#STOCK HEALTH SCORE
st.header("Summary Metrics")
total_products = len(df)
df['inventory value'] = df['unit cost'] * df['current stock']
total_value = df['inventory value'].sum()
low_stock_count = df[df['current stock'] <= df['reorder point']].shape[0]
stock_health_score = 100 * (total_products - low_stock_count) / total_products if total_products else 0


col1, col2, col3 = st.columns(3)
col1.metric("Total Products", total_products)
col2.metric("Total Inventory Value", f"${total_value:,.2f}")
col3.metric("Low Stock Items", low_stock_count)

st.progress(stock_health_score / 100)
st.caption(f"Stock Health Score: {stock_health_score:.1f}% (higher = better)")



st.header("Product Count by Category")
category_counts = df['category'].value_counts()
st.bar_chart(category_counts)

st.header("Inventory Value by Category")
value_by_category = df.groupby('category')['inventory value'].sum()

# Plot pie chart
fig, ax = plt.subplots()
ax.pie(value_by_category, labels=value_by_category.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio = perfect circle
st.pyplot(fig)

st.header("Reorder Alerts")
low_stock = df[df['current stock'] <= df['reorder point']]

if not low_stock.empty:
    st.warning(f"{len(low_stock)} product(s) need to be reordered soon!")
    st.dataframe(low_stock[['product name', 'current stock', 'reorder point']])
else:
    st.success("All products are sufficiently stocked.")

st.header("Download Inventory Report")

csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Full Inventory Report (CSV)",
    data=csv,
    file_name="inventory_report.csv",
    mime="text/csv",
)