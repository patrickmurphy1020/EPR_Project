import pandas as pd

# Load DMA sheet with correct header row
df = pd.read_excel(
    "../data/real/nhs/digital_maturity_assessment.xlsx",
    sheet_name="SC - 2025 Pillar Summary",
    header=10
)

# Keep only Acute trusts
df = df[df["Care Setting"] == "Acute"]

# Rename columns to standard names
df = df.rename(columns={
    "Provider": "Org Name",
    "Well Led": "Pillar_WellLed",
    "Ensure Smart Foundations": "Pillar_SmartFoundations",
    "Safe Practice": "Pillar_SafePractice",
    "Support Workforce": "Pillar_Workforce",
    "Empower People": "Pillar_EmpowerPeople",
    "Improve Care": "Pillar_ImproveCare",
    "Healthy Populations": "Pillar_HealthyPopulations"
})

# Add Org Code by merging with workforce (which has Org Code + Org Name)
workforce = pd.read_csv("../data/processed/workforce_clean.csv")
dma = df.merge(workforce[["Org Code", "Org Name"]], on="Org Name", how="left")

# Drop rows without Org Code (non-acute or unmatched)
dma = dma.dropna(subset=["Org Code"])

# Save cleaned DMA dataset
dma.to_csv("../data/processed/digital_maturity_clean.csv", index=False)

print("✅ DMA cleaned successfully!")
print(dma.head())
