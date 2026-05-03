import pandas as pd

df = pd.read_csv("../data/processed/outpatient_activity_clean.csv")

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

print("\n=== SUMMARY STATISTICS (Totals) ===")
total_cols = [
    "Total_Attended",
    "Total_DNA",
    "Total_Cancelled_Patient",
    "Total_Cancelled_Hospital",
    "Total_Appointments"
]
print(df[total_cols].describe())

print("\n=== CHECK FOR NEGATIVE VALUES (should not exist) ===")
for col in total_cols:
    bad = df[df[col] < 0]
    if not bad.empty:
        print(f"⚠️ Negative values found in {col}:")
        print(bad)
    else:
        print(f"{col}: OK")

print("\n=== SAMPLE TRUST NAMES ===")
print(df["TrustName"].sample(10))
