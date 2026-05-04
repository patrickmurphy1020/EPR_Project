import pandas as pd

# Load raw RTT file
df = pd.read_csv("../data/real/nhs/rtt_waiting_list.csv")

print("\n=== BASIC INFO ===")
print(df.info())

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== COLUMN NAMES ===")
print(list(df.columns))

print("\n=== ROW COUNT ===")
print(len(df))

print("\n=== UNIQUE RTT PART TYPES ===")
if "RTT Part Type" in df.columns:
    print(df["RTT Part Type"].unique())
else:
    print("Column 'RTT Part Type' not found")

print("\n=== UNIQUE TREATMENT FUNCTION CODES (first 20) ===")
if "Treatment Function Code" in df.columns:
    print(df["Treatment Function Code"].unique()[:20])
else:
    print("Column 'Treatment Function Code' not found")

print("\n=== SAMPLE PROVIDER CODES ===")
if "Provider Org Code" in df.columns:
    print(df["Provider Org Code"].sample(10))
else:
    print("Column 'Provider Org Code' not found")

print("\n=== CHECK FOR WEEK BUCKET COLUMNS ===")
week_cols = [col for col in df.columns if "Weeks" in col]
print(f"Found {len(week_cols)} week bucket columns")
print(week_cols[:10])

print("\n=== MISSING VALUES PER COLUMN ===")
print(df.isna().sum())
