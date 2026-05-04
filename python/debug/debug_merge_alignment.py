import pandas as pd

datasets = {
    "DMA": pd.read_csv("../data/processed/digital_maturity_clean.csv"),
    "RTT": pd.read_csv("../data/processed/rtt_waiting_list_clean.csv"),
    "OPA": pd.read_csv("../data/processed/outpatient_activity_clean.csv"),
    "DM01": pd.read_csv("../data/processed/diagnostics_dm01_clean.csv"),
    "AE": pd.read_csv("../data/processed/ae_attendances_clean.csv"),
    "Workforce": pd.read_csv("../data/processed/workforce_clean.csv"),
}

print("\n=== ORG CODE COUNTS ===")
for name, df in datasets.items():
    print(f"{name}: {df['Org Code'].nunique()} unique codes")

print("\n=== ORG CODE INTERSECTIONS WITH DMA ===")
dma_codes = set(datasets["DMA"]["Org Code"].unique())
for name, df in datasets.items():
    overlap = dma_codes.intersection(set(df["Org Code"].unique()))
    print(f"DMA ∩ {name}: {len(overlap)}")

print("\n=== ORG CODES IN DMA BUT MISSING FROM EACH DATASET ===")
for name, df in datasets.items():
    missing = dma_codes - set(df["Org Code"].unique())
    print(f"\nMissing in {name}: {len(missing)}")
    if len(missing) <= 20:
        print(sorted(list(missing)))
