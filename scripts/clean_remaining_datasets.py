import pandas as pd
import os

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
REPORT_DIR = "reports"

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

data_dictionary = []

# ====================================================
# Helper Function
# ====================================================

def save_dataset(df, filename, description):

    output_path = os.path.join(
        PROCESSED_DIR,
        filename
    )

    df.to_csv(
        output_path,
        index=False
    )

    data_dictionary.append(
        {
            "dataset": filename,
            "description": description,
            "columns": list(df.columns),
            "dtypes": dict(df.dtypes.astype(str))
        }
    )

    print(f"Saved {filename}")


# ====================================================
# 1. AUM BY FUND HOUSE
# ====================================================

df = pd.read_csv(
    f"{RAW_DIR}/aum_by_fund_house.csv"
)

df["date"] = pd.to_datetime(df["date"])

numeric_cols = [
    "aum_lakh_crore",
    "aum_crore",
    "num_schemes"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df.drop_duplicates()

save_dataset(
    df,
    "aum_by_fund_house_cleaned.csv",
    "Monthly AUM by Fund House"
)

# ====================================================
# 2. BENCHMARK INDICES
# ====================================================

df = pd.read_csv(
    f"{RAW_DIR}/benchmark_indices.csv"
)

df["date"] = pd.to_datetime(df["date"])

df["close_value"] = pd.to_numeric(
    df["close_value"],
    errors="coerce"
)

df = df[df["close_value"] > 0]

df = df.drop_duplicates()

save_dataset(
    df,
    "benchmark_indices_cleaned.csv",
    "Benchmark Index Values"
)

# ====================================================
# 3. CATEGORY INFLOWS
# ====================================================

df = pd.read_csv(
    f"{RAW_DIR}/category_inflows.csv"
)

df["month"] = pd.to_datetime(
    df["month"]
)

df["net_inflow_crore"] = pd.to_numeric(
    df["net_inflow_crore"],
    errors="coerce"
)

df = df.drop_duplicates()

save_dataset(
    df,
    "category_inflows_cleaned.csv",
    "Monthly Category Wise Net Inflows"
)

# ====================================================
# 4. FUND MASTER
# ====================================================

df = pd.read_csv(
    f"{RAW_DIR}/fund_master.csv"
)

df["launch_date"] = pd.to_datetime(
    df["launch_date"],
    errors="coerce"
)

numeric_cols = [
    "expense_ratio_pct",
    "exit_load_pct",
    "min_sip_amount",
    "min_lumpsum_amount"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["amfi_code"] = pd.to_numeric(
    df["amfi_code"],
    errors="coerce"
)

df = df.drop_duplicates(
    subset=["amfi_code"]
)

save_dataset(
    df,
    "fund_master_cleaned.csv",
    "Master Table of Mutual Funds"
)

# ====================================================
# 5. INDUSTRY FOLIO COUNT
# ====================================================

df = pd.read_csv(
    f"{RAW_DIR}/industry_folio_count.csv"
)

df["month"] = pd.to_datetime(
    df["month"]
)

for col in df.columns[1:]:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df.drop_duplicates()

save_dataset(
    df,
    "industry_folio_count_cleaned.csv",
    "Industry Folio Statistics"
)

# ====================================================
# 6. MONTHLY SIP INFLOWS
# ====================================================

df = pd.read_csv(
    f"{RAW_DIR}/monthly_sip_inflows.csv"
)

df["month"] = pd.to_datetime(
    df["month"]
)

for col in df.columns[1:]:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df.drop_duplicates()

save_dataset(
    df,
    "monthly_sip_inflows_cleaned.csv",
    "Industry SIP Statistics"
)

# ====================================================
# 7. PORTFOLIO HOLDINGS
# ====================================================

df = pd.read_csv(
    f"{RAW_DIR}/portfolio_holdings.csv"
)

df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"]
)

numeric_cols = [
    "weight_pct",
    "market_value_cr",
    "current_price_inr"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# weight validation

invalid_weights = df[
    (df["weight_pct"] < 0)
    |
    (df["weight_pct"] > 100)
]

print(
    f"Invalid weights found: {len(invalid_weights)}"
)

df = df.drop_duplicates()

save_dataset(
    df,
    "portfolio_holdings_cleaned.csv",
    "Fund Portfolio Holdings"
)

# ====================================================
# DATA DICTIONARY GENERATION
# ====================================================

with open(
    f"{REPORT_DIR}/data_dictionary.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "# Mutual Fund Data Dictionary\n\n"
    )

    for dataset in data_dictionary:

        f.write(
            f"## {dataset['dataset']}\n\n"
        )

        f.write(
            f"{dataset['description']}\n\n"
        )

        f.write(
            "| Column | Data Type |\n"
        )

        f.write(
            "|----------|----------|\n"
        )

        for col in dataset["columns"]:

            dtype = dataset["dtypes"][col]

            f.write(
                f"| {col} | {dtype} |\n"
            )

        f.write("\n\n")

print(
    "\nData Dictionary Created:"
)

print(
    "reports/data_dictionary.md"
)