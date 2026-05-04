import pandas as pd

# Load raw CSV without assuming header
raw = pd.read_csv("../data/real/nhs/ae_attendances_march2025.csv", header=None)

# ---------------------------------------------------------
# Detect header row automatically
# ---------------------------------------------------------
header_row = None
for i in range(15):  # first 15 rows is enough
    row = raw.iloc[i].astype(str).str.lower()
    if "org code" in row.values and "a&e attendances type 1" in row.values:
        header_row = i
        break

if header_row is None:
    raise ValueError("❌ Could not detect header row. Check the CSV manually.")

print(f"\n=== HEADER ROW DETECTED AT LINE {header_row} ===")

# Load properly with detected header
df = pd.read_csv("../data/real/nhs/ae_attendances_march2025.csv", header=header_row)

print("\n=== BASIC INFO ===")
print(df.info())

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== COLUMN NAMES ===")
print(list(df.columns))

print("\n=== ROW COUNT ===")
print(len(df))

# ---------------------------------------------------------
# Identify key columns
# ---------------------------------------------------------
key_cols = [
    "Org Code",
    "Org name",
    "A&E attendances Type 1",
    "Attendances over 4hrs Type 1",
    "Patients who have waited 4-12 hs from DTA to admission",
    "Patients who have waited 12+ hrs from DTA to admission",
    "Emergency admissions via A&E - Type 1"
]

print("\n=== CHECK FOR KEY FIELDS ===")
for col in key_cols:
    found = any(col.lower() in c.lower() for c in df.columns)
    print(f"{col}: {'FOUND' if found else '❌ MISSING'}")

# ---------------------------------------------------------
# Show sample Type 1 trusts
# ---------------------------------------------------------
type1_col = [c for c in df.columns if "a&e attendances type 1" in c.lower()][0]

print("\n=== SAMPLE TYPE 1 TRUSTS (attendances > 0) ===")
sample = df[df[type1_col] > 0].head(10)
print(sample[["Org Code", "Org name", type1_col]])

# ---------------------------------------------------------
# Missing values
# ---------------------------------------------------------
print("\n=== MISSING VALUES PER COLUMN ===")
print(df.isna().sum())

# ---------------------------------------------------------
# Summary stats for Type 1 metrics
# ---------------------------------------------------------
metric_cols = [
    c for c in df.columns
    if "type 1" in c.lower() or "12" in c.lower() or "4-12" in c.lower()
]

print("\n=== SUMMARY STATISTICS (TYPE 1 METRICS) ===")
print(df[metric_cols].describe())
