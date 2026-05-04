import pandas as pd

# Load raw DMA sheet
df = pd.read_excel(
    "../data/real/nhs/digital_maturity_assessment.xlsx",
    sheet_name="SC - 2025 Pillar Summary",
    header=10
)

# --- CLEAN CARE SETTING ---
df["Care Setting"] = df["Care Setting"].astype(str).str.strip().str.lower()

# Keep only acute providers
df = df[df["Care Setting"].str.contains("acute")]

# --- CLEAN TRUST NAMES ---
df["Provider"] = df["Provider"].astype(str).str.strip().str.title()

# Rename pillar columns
df = df.rename(columns={
    "Provider": "TrustName",
    "Well Led": "Pillar_WellLed",
    "Ensure Smart Foundations": "Pillar_SmartFoundations",
    "Safe Practice": "Pillar_SafePractice",
    "Support Workforce": "Pillar_Workforce",
    "Empower People": "Pillar_EmpowerPeople",
    "Improve Care": "Pillar_ImproveCare",
    "Healthy Populations": "Pillar_HealthyPopulations"
})

# Load workforce (contains Org Code + Org Name)
workforce = pd.read_csv("../data/processed/workforce_clean.csv")

# Clean workforce names to match DMA
workforce["Org Name Clean"] = workforce["Org Name"].str.strip().str.title()
df["TrustName Clean"] = df["TrustName"].str.strip().str.title()

# Merge using cleaned names
dma = df.merge(
    workforce[["Org Code", "Org Name", "Org Name Clean"]],
    left_on="TrustName Clean",
    right_on="Org Name Clean",
    how="left"
)

# Drop rows without Org Code
dma = dma.dropna(subset=["Org Code"])

# Drop helper columns
dma = dma.drop(columns=["Org Name Clean", "TrustName Clean"])

# Save cleaned DMA
dma.to_csv("../data/processed/digital_maturity_clean.csv", index=False)

print("DMA cleaned successfully!")
print("Rows:", len(dma))
print(dma.head())
