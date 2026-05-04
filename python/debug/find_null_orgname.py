import pandas as pd

df = pd.read_csv("../data/processed/master_trust_dataset_engineered.csv")

# Show rows where Org Name is missing
null_rows = df[df["Org Name"].isna() | (df["Org Name"] == "")]
print(null_rows)
