import pandas as pd

# Load the validated A&E CSV (header already correct)
df = pd.read_csv("../data/real/nhs/ae_attendances_march2025.csv")

# ---------------------------------------------------------
# 1. Standardise column names (strip spaces)
# ---------------------------------------------------------
df.columns = df.columns.str.strip()

# ---------------------------------------------------------
# 2. Keep only the columns we need (Option A)
# ---------------------------------------------------------
keep_cols = [
    "Org Code",
    "Org name",
    "A&E attendances Type 1",
    "Attendances over 4hrs Type 1",
    "Patients who have waited 4-12 hs from DTA to admission",
    "Patients who have waited 12+ hrs from DTA to admission",
    "Emergency admissions via A&E - Type 1"
]

df = df[keep_cols]

# ---------------------------------------------------------
# 3. Filter to acute NHS trusts only
#    ODS codes: start with R and length = 3
# ---------------------------------------------------------
df = df[df["Org Code"].str.match(r"^R[A-Z0-9]{2}$")]

# ---------------------------------------------------------
# 4. Filter to Type 1 providers (attendances > 0)
# ---------------------------------------------------------
df = df[df["A&E attendances Type 1"] > 0]

# ---------------------------------------------------------
# 5. Reset index
# ---------------------------------------------------------
df = df.reset_index(drop=True)

# ---------------------------------------------------------
# 6. Save cleaned dataset
# ---------------------------------------------------------
df.to_csv("../data/processed/ae_attendances_clean.csv", index=False)

print("✅ A&E Type 1 cleaned successfully!")
print(f"Rows after filtering: {len(df)}")
print(df.head())
