import pandas as pd
import os

# ============================================================
#  CLEAN DIGITAL MATURITY ASSESSMENT (DMA)
# ============================================================

dma_path = "../data/real/nhs/digital_maturity_assessment.xlsx"

# -----------------------------
# Load trust-level pillar scores (Sheet 2)
# -----------------------------
pillars = pd.read_excel(dma_path, sheet_name="SC - 2025 Pillar Summary")

# Clean column names
pillars.columns = (
    pillars.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.lower()
)

# Rename pillar columns
pillars = pillars.rename(columns={
    "provider": "TrustName",
    "ics": "ICSName",
    "region": "Region",
    "well_led": "DMAWellLed",
    "ensure_smart_foundations": "DMASmartFoundations",
    "safe_practice": "DMASafePractice",
    "support_workforce": "DMAWorkforce",
    "empower_people": "DMAEmpowerPeople",
    "improve_care": "DMAImproveCare",
    "healthy_populations": "DMAHealthyPopulations"
})

# -----------------------------
# Load trust-level overall scores (Sheet 3)
# -----------------------------
overall = pd.read_excel(dma_path, sheet_name="SC - 24 vs 25 Overall DMA")

overall.columns = (
    overall.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.lower()
)

overall = overall.rename(columns={
    "provider": "TrustName",
    "ics": "ICSName",
    "region": "Region",
    "2025_average": "DMAOverall2025",
    "2024_average": "DMAOverall2024"
})

# -----------------------------
# Merge pillar + overall scores
# -----------------------------
dma_merged = pd.merge(
    pillars,
    overall[["TrustName", "DMAOverall2025", "DMAOverall2024"]],
    on="TrustName",
    how="left"
)

# -----------------------------
# Filter to Leeds Teaching Hospitals NHS Trust
# -----------------------------
dma_ltht = dma_merged[
    dma_merged["TrustName"].str.contains("Leeds Teaching Hospitals", case=False, na=False)
]

# -----------------------------
# Save cleaned dataset
# -----------------------------
os.makedirs("../data/processed", exist_ok=True)
dma_ltht.to_csv("../data/processed/digital_maturity_clean.csv", index=False)

print("Digital Maturity dataset cleaned and saved to /data/processed/")
