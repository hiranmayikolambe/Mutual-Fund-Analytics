from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

txn = pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
)

perf = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded successfully")