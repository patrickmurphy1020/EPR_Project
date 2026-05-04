import pandas as pd

# Load raw CSV but DO NOT assume header row
raw = pd.read_csv("../data/real/nhs/diagnostics_dm01.csv", header=None)

# ---------------------------------------------------------
# Detect the header row automatically
# ---------------------------------------------------------
header_row = None
for i in range(20):  # look at first 20 rows
    row = raw.iloc[i].astype(str).str.lower()
    if "provider code" in row.values and "provider name" in row.values:
        header_row = i
        break

if header_row is None:
    raise ValueError("❌ Could not find header row. Check the CSV manually.")

print(f"\n=== HEADER ROW DETECTED AT LINE {header_row} ===")

# Now load the file properly using that header row
df = pd.read_csv("../data/real/nhs/diagnostics_dm01.csv", header=header_row)

print("\n=== BASIC INFO ===")
print(df.info())

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== COLUMN NAMES ===")
print(list(df.columns))

print("\n=== ROW COUNT ===")
print(len(df))

# ---------------------------------------------------------
# Provider code check
# ---------------------------------------------------------
provider_col = None
for col in df.columns:
    if "provider code" in col.lower():
        provider_col = col
        break

print("\n=== PROVIDER CODE COLUMN ===")
print(provider_col)

if provider_col:
    print(df[provider_col].dropna().sample(10))

# ---------------------------------------------------------
# Key fields check
# ---------------------------------------------------------
expected = [
    "Total Waiting List",
    "Number waiting 6+ Weeks",
    "Number waiting 13+ Weeks",
    "Percentage waiting 6+ weeks"
]

print("\n=== CHECK FOR KEY FIELDS ===")
for col in expected:
    found = any(col.lower() in c.lower() for c in df.columns)
    print(f"{col}: {'FOUND' if found else '❌ MISSING'}")

# ---------------------------------------------------------
# Missing values
# ---------------------------------------------------------
print("\n=== MISSING VALUES PER COLUMN ===")
print(df.isna().sum())

# ---------------------------------------------------------
# Summary stats
# ---------------------------------------------------------
metric_cols = [c for c in df.columns if "waiting" in c.lower() or "percentage" in c.lower()]

print("\n=== SUMMARY STATISTICS ===")
print(df[metric_cols].describe())

# ---------------------------------------------------------
# Sample trust names
# ---------------------------------------------------------
name_col = None
for col in df.columns:
    if "provider name" in col.lower():
        name_col = col
        break

print("\n=== SAMPLE PROVIDER NAMES ===")
print(df[name_col].dropna().sample(10))
