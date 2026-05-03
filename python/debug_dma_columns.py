import pandas as pd

dma_path = "data/real/nhs/digital_maturity_assessment.xlsx"

overall = pd.read_excel(dma_path, sheet_name="SC - 24 vs 25 Overall DMA")

overall.columns = (
    overall.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.lower()
)

print(overall.columns.tolist())
