import pandas as pd

# Load raw CSV and auto-detect header row
raw = pd.read_csv("../data/real/nhs/diagnostics_dm01.csv", header=None)

# Detect header row
header_row = None
for i in range(20):
    row = raw.iloc[i].astype(str).str.lower()
    if "provider code" in row.values and "provider name" in row.values:
        header_row = i
        break

if header_row is None:
    raise ValueError("❌ Could not detect header row.")

# Load clean table
df = pd.read_csv("../data/real/nhs/diagnostics_dm01.csv", header=header_row)

# ---------------------------------------------------------
# 1. Drop junk columns (Unnamed)
# ---------------------------------------------------------
df = df.loc[:, ~df.columns.str.contains("Unnamed")]

# ---------------------------------------------------------
# 2. Standardise column names (strip spaces)
# ---------------------------------------------------------
df.columns = df.columns.str.strip()

# ---------------------------------------------------------
# 3. Keep only the columns we need (Option A)
# ---------------------------------------------------------
keep_cols = [
    "Provider Code",
    "Provider Name",
    "Total Waiting List",
    "Number waiting 6+ Weeks",
    "Number waiting 13+ Weeks",
    "Percentage waiting 6+ weeks"
]

df = df[keep_cols]

# ---------------------------------------------------------
# 4. Convert numeric fields
# ---------------------------------------------------------
num_cols = [
    "Total Waiting List",
    "Number waiting 6+ Weeks",
    "Number waiting 13+ Weeks",
    "Percentage waiting 6+ weeks"
]

for col in num_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("%", "", regex=False)
        .astype(float)
    )

# ---------------------------------------------------------
# 5. Filter to Acute NHS Trusts only
#    ODS codes: start with R and length = 3
# ---------------------------------------------------------

# Drop rows with missing provider codes
df = df.dropna(subset=["Provider Code"])

# Filter to acute NHS trusts
df = df[df["Provider Code"].str.match(r"^R[A-Z0-9]{2}$")]

# ---------------------------------------------------------
# 6. Drop rows with missing provider codes
# ---------------------------------------------------------
df = df.dropna(subset=["Provider Code"])

# ---------------------------------------------------------
# 7. Reset index
# ---------------------------------------------------------
df = df.reset_index(drop=True)

# ---------------------------------------------------------
# 8. Save cleaned dataset
# ---------------------------------------------------------
df.to_csv("../data/processed/diagnostics_dm01_clean.csv", index=False)

print("✅ DM01 cleaned successfully!")
print(f"Rows after filtering: {len(df)}")
print(df.head())
