import pandas as pd

# Load the workforce CSV
df = pd.read_csv("../data/real/nhs/workforce_march2025.csv")

print("\n=== BASIC INFO ===")
print(df.info())

print("\n=== FIRST 10 ROWS ===")
print(df.head(10))

print("\n=== COLUMN NAMES ===")
print(list(df.columns))

print("\n=== ROW COUNT ===")
print(len(df))

# ---------------------------------------------------------
# Identify key expected columns
# ---------------------------------------------------------
expected_cols = [
    "Org Code",
    "Org Name",
    "Staff Group",
    "FTE",
    "Headcount"
]

print("\n=== CHECK FOR KEY FIELDS ===")
for col in expected_cols:
    found = any(col.lower() in c.lower() for c in df.columns)
    print(f"{col}: {'FOUND' if found else '❌ MISSING'}")

# ---------------------------------------------------------
# Show sample rows for acute trusts (ODS codes starting with R)
# ---------------------------------------------------------
print("\n=== SAMPLE ACUTE TRUST ROWS (ODS starts with R) ===")
sample = df[df["Org Code"].str.match(r"^R[A-Z0-9]{2}$")].head(10)
print(sample)

# ---------------------------------------------------------
# Staff group distribution
# ---------------------------------------------------------
print("\n=== UNIQUE STAFF GROUPS ===")
print(df["Staff Group"].unique())

# ---------------------------------------------------------
# Missing values
# ---------------------------------------------------------
print("\n=== MISSING VALUES PER COLUMN ===")
print(df.isna().sum())
