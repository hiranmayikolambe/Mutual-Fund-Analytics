import pandas as pd
df = pd.read_csv("data/raw/nav_history.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV within fund
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Remove invalid NAVs
df = df[df["nav"] > 0]

print(df.isnull().sum())

df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)
print("Duplicate rows:", df.duplicated().sum())

print("Negative NAV:")
print((df["nav"] <= 0).sum())