import pandas as pd

# Load cleaned RTT dataset
df = pd.read_csv("../data/processed/rtt_waiting_list_clean.csv")

print("\n=== BASIC INFO ===")
print(df.info())

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== ROW COUNT ===")
print(len(df))

print("\n=== DUPLICATE TRUST NAMES ===")
dupes = df[df.duplicated(subset=["TrustName"], keep=False)]
print(dupes if not dupes.empty else "No duplicates found")

print("\n=== MISSING VALUES PER COLUMN ===")
print(df.isna().sum())

print("\n=== SUMMARY STATISTICS (RTT Metrics) ===")
metric_cols = [
    "Total_Waiting_List",
    "WL_52w",
    "WL_65w",
    "WL_78w",
    "WL_104w"
]
print(df[metric_cols].describe())

print("\n=== CHECK FOR NEGATIVE VALUES (should not exist) ===")
for col in metric_cols:
    bad = df[df[col] < 0]
    if not bad.empty:
        print(f"⚠️ Negative values found in {col}:")
        print(bad)
    else:
        print(f"{col}: OK")

print("\n=== SAMPLE TRUST NAMES ===")
print(df["TrustName"].sample(10))
