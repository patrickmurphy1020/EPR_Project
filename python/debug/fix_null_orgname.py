import pandas as pd

# Load engineered master dataset
df = pd.read_csv("../data/processed/master_trust_dataset_engineered.csv")

# Load workforce (has Org Code + Org Name)
workforce = pd.read_csv("../data/processed/workforce_clean.csv")

# Keep only the columns we need from workforce
workforce_small = workforce[["Org Code", "Org Name"]].drop_duplicates()

# Merge to bring in Org Name where missing
df = df.merge(
    workforce_small,
    on="Org Code",
    how="left",
    suffixes=("", "_wf")
)

# If Org Name is missing, fill from workforce
df["Org Name"] = df["Org Name"].fillna(df["Org Name_wf"])

# Drop helper column
df = df.drop(columns=["Org Name_wf"])

# Drop any rows that STILL have no Org Name or Org Code (true orphans)
df = df.dropna(subset=["Org Code", "Org Name"])

# Save back
df.to_csv("../data/processed/master_trust_dataset_engineered.csv", index=False)

print("Fixed missing Org Name values and removed any orphan rows.")
