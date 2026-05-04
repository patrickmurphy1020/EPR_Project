import pandas as pd

# Load the correct sheet from the DMA Excel file
df = pd.read_excel(
    "../data/real/nhs/digital_maturity_assessment.xlsx",
    sheet_name="SC - 2025 Pillar Summary"
)

print("\n=== DMA RAW COLUMNS ===")
print(df.columns.tolist())

print("\n=== FIRST 10 ROWS ===")
print(df.head(10))
