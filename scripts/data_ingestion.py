import pandas as pd
import os

DATA_DIR = "data/raw"

files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]

for file in files:
    print("=" * 80)
    print(f"Dataset: {file}")

    path = os.path.join(DATA_DIR, file)

    df = pd.read_csv(path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())