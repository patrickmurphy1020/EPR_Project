import pandas as pd

files = [
    "digital_maturity_clean.csv",
    "rtt_waiting_list_clean.csv",
    "outpatient_activity_clean.csv",
    "diagnostics_dm01_clean.csv",
    "ae_attendances_clean.csv",
    "workforce_clean.csv"
]

for f in files:
    df = pd.read_csv(f"../data/processed/{f}")
    print("\n=== FILE:", f, "===")
    print(df.columns.tolist())
