import pandas as pd

df = pd.read_csv(
    "data/raw/scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# anomaly flags

anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print(
    "Return anomalies:",
    len(anomalies)
)

# expense ratio validation

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "Expense anomalies:",
    len(invalid_expense)
)

df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)