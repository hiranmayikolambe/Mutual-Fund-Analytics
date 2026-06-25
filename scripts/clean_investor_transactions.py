import pandas as pd
df = pd.read_csv(
    "data/raw/investor_transactions.csv"
)

# date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# transaction type standardization

mapping = {
    "sip":"SIP",
    "SIP":"SIP",
    "systematic investment plan":"SIP",

    "lumpsum":"Lumpsum",
    "Lump Sum":"Lumpsum",

    "redemption":"Redemption",
    "Redeem":"Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .replace(mapping)
)

# amount validation
invalid_amount = df[df["amount_inr"] <= 0]

print("Invalid Amount:", len(invalid_amount))

df = df[df["amount_inr"] > 0]

# KYC validation

allowed = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = (
    ~df["kyc_status"].isin(allowed)
)

print(
    "Invalid KYC:",
    invalid_kyc.sum()
)

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)
print(
df["kyc_status"].value_counts()
)