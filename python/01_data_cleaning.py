import pandas as pd

# Correct path (script is inside python/)
dma_path = "../data/real/nhs/digital_maturity_assessment.xlsx"

# ============================================================
# LOAD SHEET 2 — PILLAR SCORES (SC - 2025 Pillar Summary)
# ============================================================
pillars = pd.read_excel(
    dma_path,
    sheet_name="SC - 2025 Pillar Summary",
    skiprows=10
)

# Clean column names
pillars.columns = (
    pillars.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.lower()
)

# Drop empty first column if present
if "unnamed:_0" in pillars.columns:
    pillars = pillars.drop(columns=["unnamed:_0"])

# Filter to Secondary Care only
pillars = pillars[pillars["care_setting"] == "Secondary Care"]

# Rename pillar columns
pillars = pillars.rename(columns={
    "provider": "TrustName",
    "well_led": "Pillar_WellLed",
    "ensure_smart_foundations": "Pillar_SmartFoundations",
    "safe_practice": "Pillar_SafePractice",
    "support_workforce": "Pillar_Workforce",
    "empower_people": "Pillar_EmpowerPeople",
    "improve_care": "Pillar_ImproveCare",
    "healthy_populations": "Pillar_HealthyPopulations"
})

# Select only needed columns
pillars = pillars[[
    "TrustName",
    "Pillar_WellLed",
    "Pillar_SmartFoundations",
    "Pillar_SafePractice",
    "Pillar_Workforce",
    "Pillar_EmpowerPeople",
    "Pillar_ImproveCare",
    "Pillar_HealthyPopulations"
]]

# ============================================================
# LOAD SHEET 3 — OVERALL SCORES (SC - 24 vs 25 Overall DMA)
# ============================================================
overall = pd.read_excel(
    dma_path,
    sheet_name="SC - 24 vs 25 Overall DMA",
    skiprows=10
)

# Clean column names
overall.columns = (
    overall.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.lower()
)

# Drop empty first column
if "unnamed:_0" in overall.columns:
    overall = overall.drop(columns=["unnamed:_0"])

# Filter to Secondary Care only
overall = overall[overall["care_setting"] == "Secondary Care"]

# Rename columns
overall = overall.rename(columns={
    "provider": "TrustName",
    "2025_average": "DMAOverall2025",
    "2024_average": "DMAOverall2024"
})

# Select only needed columns
overall = overall[[
    "TrustName",
    "DMAOverall2025",
    "DMAOverall2024"
]]

# ============================================================
# MERGE BOTH SHEETS
# ============================================================
merged = pd.merge(
    pillars,
    overall,
    on="TrustName",
    how="left"
)

# Remove blank rows (trailing junk from Excel)
merged = merged.dropna(subset=["TrustName"])

# ============================================================
# SAVE CLEANED OUTPUT
# ============================================================
output_path = "../data/processed/digital_maturity_clean.csv"
merged.to_csv(output_path, index=False)

print("Digital Maturity dataset cleaned and saved to:", output_path)
