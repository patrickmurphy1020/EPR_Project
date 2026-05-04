import pandas as pd

df = pd.read_excel("../data/real/nhs/digital_maturity_assessment.xlsx")  # adjust filename if needed

print(df.columns.tolist())
print(df.head())
