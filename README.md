# Supply Chain Analytics Dashboard

A medium-tier inventory analytics dashboard built with **Streamlit**, **Pandas**, and **SQLite** — designed for early-stage startups and lean ops teams to monitor stock levels, reorder needs, inventory value, and overall supply chain health.

### Live Demo
[Click to view the live app on Streamlit](https://supplychaindash.streamlit.app)

---

## 🔍 Features

-  **Filterable Inventory Table** – search by product name and filter by category
-  **Reorder Alerts** – automatically flags low-stock items
-  **Summary Metrics** – total products, total inventory value, and stock health score
-  **Bar & Pie Charts** – visual insights by category and value
-  **Downloadable CSV Reports** – export inventory for reporting or team syncs
-  **Offline SQLite Integration** – plug in real warehouse or supplier data

---

##  Ideal Use Case

This tool is ideal for:
-  Startups with 1–10 team members running **pilot inventory rounds**
-  Ops managers overseeing < 1000 SKUs
-  Teams not yet on a full ERP system, but need data-driven inventory visibility

---

## Tech Stack

| Tool       | Purpose                           |
|------------|-----------------------------------|
| `Streamlit` | UI & interactivity                |
| `Pandas`    | Data filtering, grouping, metrics |
| `Matplotlib`| Pie charts                        |
| `SQLite`    | Lightweight inventory database    |

---

## Getting Started 

```bash
# Clone this repository
git clone https://github.com/audreykchan/supplychaindash.git
cd supplychaindash

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run supply_dashboard.py
