import pandas as pd

# Load raw ESR workforce file
df = pd.read_csv("../data/real/nhs/workforce_march2025.csv")

# ---------------------------------------------------------
# 1. Filter to March 2025 only
# ---------------------------------------------------------
df["Date"] = pd.to_datetime(df["Date"])
df = df[df["Date"] == "2025-03-31"]

# ---------------------------------------------------------
# 2. Filter to acute NHS trusts (ODS codes start with R, length = 3)
# ---------------------------------------------------------
df = df[df["Org Code"].str.match(r"^R[A-Z0-9]{2}$")]

# ---------------------------------------------------------
# 3. Keep only FTE rows (ignore headcount)
# ---------------------------------------------------------
df = df[df["Data Type"] == "FTE"]

# ---------------------------------------------------------
# 4. Map ESR staff groups to simplified categories (Option A)
# ---------------------------------------------------------
mapping = {
    "HCHS Doctors": "Medical",
    "Consultant": "Medical",
    "Associate Specialist": "Medical",
    "Specialty Doctor": "Medical",
    "Staff Grade": "Medical",
    "Hospital Practitioner / Clinical Assistant": "Medical",
    "Other HCHS Doctor Grades": "Medical",
    "Specialty Registrar": "Medical",
    "Core Training": "Medical",
    "Foundation Doctor Year 1": "Medical",
    "Foundation Doctor Year 2": "Medical",

    "Nurses & health visitors": "Nursing",
    "Midwives": "Nursing",

    "Scientific, therapeutic & technical staff": "ST&T",

    "Support to clinical staff": "Support",
    "Support to doctors, nurses & midwives": "Support",
    "Support to ST&T staff": "Support",
    "Support to ambulance staff": "Support",

    "NHS infrastructure support": "Admin",
    "Senior managers": "Admin",
    "Managers": "Admin",
    "Central functions": "Admin",
    "Hotel, property & estates": "Admin",

    "Ambulance staff": "Ambulance",

    "Total": "Total"
}

df["Category"] = df["Staff Group"].map(mapping)

# Drop rows that don't map to a main category
df = df.dropna(subset=["Category"])

# ---------------------------------------------------------
# 5. Aggregate FTE by trust + category
# ---------------------------------------------------------
agg = df.groupby(["Org Code", "Org Name", "Category"])["Total"].sum().reset_index()

# ---------------------------------------------------------
# 6. Pivot to wide format (one row per trust)
# ---------------------------------------------------------
clean = agg.pivot_table(
    index=["Org Code", "Org Name"],
    columns="Category",
    values="Total",
    fill_value=0
).reset_index()

# ---------------------------------------------------------
# 7. Save cleaned dataset
# ---------------------------------------------------------
clean.to_csv("../data/processed/workforce_clean.csv", index=False)

print("✅ Workforce cleaned successfully!")
print(f"Rows after filtering: {len(clean)}")
print(clean.head())
