import pandas as pd

dma_path = "../data/real/nhs/digital_maturity_assessment.xlsx"

df = pd.read_excel(
    dma_path,
    sheet_name="SC - 2025 Pillar Summary",
    skiprows=10
)

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.lower()
)

if "unnamed:_0" in df.columns:
    df = df.drop(columns=["unnamed:_0"])

print(df["care_setting"].unique())
