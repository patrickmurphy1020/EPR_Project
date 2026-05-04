import pandas as pd

files = {
    "DMA": "../data/processed/digital_maturity_clean.csv",
    "RTT": "../data/processed/rtt_waiting_list_clean.csv",
    "OPA": "../data/processed/outpatient_activity_clean.csv",
    "DM01": "../data/processed/diagnostics_dm01_clean.csv",
    "AE": "../data/processed/ae_attendances_clean.csv",
    "Workforce": "../data/processed/workforce_clean.csv",
}

for name, path in files.items():
    print(f"\n=== {name} COLUMNS ===")
    df = pd.read_csv(path)
    print(df.columns.tolist())
    print(f"Rows: {len(df)}")
