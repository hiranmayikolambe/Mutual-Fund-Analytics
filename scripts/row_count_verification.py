import sqlite3

conn = sqlite3.connect(
    "database/bluestock_mf.db"
)

tables = [
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:

    count = conn.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(table,count)