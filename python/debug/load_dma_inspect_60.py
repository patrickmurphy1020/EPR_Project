import pandas as pd

df = pd.read_excel(
    "../data/real/nhs/digital_maturity_assessment.xlsx",
    sheet_name="SC - 2025 Pillar Summary",
    header=None
)

pd.set_option("display.max_rows", 200)
pd.set_option("display.max_columns", 50)

print(df.head(60))
