import pandas as pd

# Load DMA sheet with correct header row
df = pd.read_excel(
    "../data/real/nhs/digital_maturity_assessment.xlsx",
    sheet_name="SC - 2025 Pillar Summary",
    header=10
)

# Keep only Acute trusts
df = df[df["Care Setting"] == "Acute"]

# Rename columns
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

# Load workforce to get Org Code + Org Name
workforce = pd.read_csv("../data/processed/workforce_clean.csv")

# Merge DMA with workforce on TrustName = Org Name
dma = df.merge(
    workforce[["Org Code", "Org Name"]],
    left_on="TrustName",
    right_on="Org Name",
    how="left"
)

# Drop rows without Org Code
dma = dma.dropna(subset=["Org Code"])

# Drop junk columns
dma = dma[[
    "Org Code", "Org Name", "TrustName",
    "Pillar_WellLed", "Pillar_SmartFoundations", "Pillar_SafePractice",
    "Pillar_Workforce", "Pillar_EmpowerPeople", "Pillar_ImproveCare",
    "Pillar_HealthyPopulations"
]]

# Save cleaned DMA dataset
dma.to_csv("../data/processed/digital_maturity_clean.csv", index=False)

print("✅ DMA cleaned successfully!")
print(dma.head())
