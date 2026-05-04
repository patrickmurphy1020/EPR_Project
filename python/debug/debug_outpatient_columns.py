import pandas as pd

df = pd.read_csv("../data/real/nhs/outpatient_activity.csv")

print("\n=== UNIQUE GEOGRAPHY_LEVEL ===")
print(df["GEOGRAPHY_LEVEL"].unique())

print("\n=== UNIQUE MEASURE_TYPE ===")
print(df["MEASURE_TYPE"].unique()[:50])  # first 50

print("\n=== UNIQUE MEASURE (first 50) ===")
print(df["MEASURE"].unique()[:50])
