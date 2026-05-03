import pandas as pd

dma_path = "../data/real/nhs/digital_maturity_assessment.xlsx"

# CHANGE THIS to inspect Sheet 2 or Sheet 3
sheet = "SC - 2025 Pillar Summary"   # or: "SC - 24 vs 25 Overall DMA"

df = pd.read_excel(
    dma_path,
    sheet_name=sheet,
    skiprows=10   # skip title block + junk rows
)

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.lower()
)

print(df.columns.tolist())
