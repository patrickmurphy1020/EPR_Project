import pandas as pd

df = pd.read_csv("../data/processed/digital_maturity_clean.csv")
print(df.columns.tolist())
print(df.head())
