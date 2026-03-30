import csv
import sqlite3

conn = sqlite3.connect("etl.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER,
    customer_name TEXT,
    amount REAL
)
""")

with open("orders.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(
            "INSERT INTO orders VALUES (?, ?, ?)",
            (row["order_id"], row["customer_name"], row["amount"])
        )

conn.commit()
conn.close()