import pandas as pd

# ---------------------------------------------------------
# Load all cleaned datasets
# ---------------------------------------------------------
dma = pd.read_csv("../data/processed/digital_maturity_clean.csv")
rtt = pd.read_csv("../data/processed/rtt_waiting_list_clean.csv")
opa = pd.read_csv("../data/processed/outpatient_activity_clean.csv")
dm01 = pd.read_csv("../data/processed/diagnostics_dm01_clean.csv")
ae = pd.read_csv("../data/processed/ae_attendances_clean.csv")
workforce = pd.read_csv("../data/processed/workforce_clean.csv")

# ---------------------------------------------------------
# Standardise column names across all datasets
# ---------------------------------------------------------

# RTT + Outpatients use TrustCode
rtt = rtt.rename(columns={"TrustCode": "Org Code", "TrustName": "Org Name"})
opa = opa.rename(columns={"TrustCode": "Org Code", "TrustName": "Org Name"})

# DM01 uses Provider Code / Provider Name
dm01 = dm01.rename(columns={"Provider Code": "Org Code", "Provider Name": "Org Name"})
dm01 = dm01.drop(columns=["Org Name"], errors="ignore")   # FIX 1

# A&E uses Org Code / Org name
ae = ae.rename(columns={"Org name": "Org Name"})
ae = ae.drop(columns=["Org Name"], errors="ignore")       # FIX 2

# Workforce contains Org Name but DMA already has it
workforce = workforce.drop(columns=["Org Name"], errors="ignore")  # FIX 3

# ---------------------------------------------------------
# Start with DMA (contains Org Code + Org Name)
# ---------------------------------------------------------
master = dma.copy()

# ---------------------------------------------------------
# Merge each dataset one by one
# ---------------------------------------------------------
master = master.merge(rtt, on="Org Code", how="left")
master = master.merge(opa, on="Org Code", how="left")
master = master.merge(dm01, on="Org Code", how="left")
master = master.merge(ae, on="Org Code", how="left")
master = master.merge(workforce, on="Org Code", how="left")

# ---------------------------------------------------------
# Reorder columns (Org Code, Org Name first)
# ---------------------------------------------------------
cols = ["Org Code", "Org Name"] + [c for c in master.columns if c not in ["Org Code", "Org Name"]]
master = master[cols]

# ---------------------------------------------------------
# Save final master dataset
# ---------------------------------------------------------
master.to_csv("../data/processed/master_trust_dataset.csv", index=False)

print("✅ Master dataset created successfully!")
print(f"Rows: {len(master)}")
print(f"Columns: {len(master.columns)}")
print(master.head())
