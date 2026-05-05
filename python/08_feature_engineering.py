import pandas as pd

# Load master dataset
df = pd.read_csv("../data/processed/master_trust_dataset.csv")

# ============================
# 1. DMA FEATURES
# ============================

# Average DMA pillar score
pillar_cols = [
    "Pillar_WellLed",
    "Pillar_SmartFoundations",
    "Pillar_SafePractice",
    "Pillar_Workforce",
    "Pillar_EmpowerPeople",
    "Pillar_ImproveCare",
    "Pillar_HealthyPopulations"
]

df["DMA_Average"] = df[pillar_cols].mean(axis=1)

# ============================
# 2. RTT FEATURES (FIXED)
# ============================

den = df["Total_Waiting_List"].replace(0, pd.NA)

# Main NHS backlog measure
df["RTT_Backlog_Ratio"] = (df["WL_52w"] / den) * 100

# Additional long-wait metrics
df["RTT_65w_Ratio"] = (df["WL_65w"] / den) * 100
df["RTT_78w_Ratio"] = (df["WL_78w"] / den) * 100
df["RTT_104w_Ratio"] = (df["WL_104w"] / den) * 100



# ============================
# 3. OUTPATIENT FEATURES
# ============================

df["OPA_DNA_Rate"] = df["Total_DNA"] / df["Total_Appointments"].replace(0, pd.NA)
df["OPA_Cancelled_Rate"] = (
    df["Total_Cancelled_Patient"] + df["Total_Cancelled_Hospital"]
) / df["Total_Appointments"].replace(0, pd.NA)

# ============================
# 4. DIAGNOSTICS (DM01) FEATURES
# ============================

df["DM01_6Week_Rate"] = df["Number waiting 6+ Weeks"] / df["Total Waiting List"].replace(0, pd.NA)
df["DM01_13Week_Rate"] = df["Number waiting 13+ Weeks"] / df["Total Waiting List"].replace(0, pd.NA)

# ============================
# 5. A&E FEATURES
# ============================

df["AE_4hr_Breach_Rate"] = df["Attendances over 4hrs Type 1"] / df["A&E attendances Type 1"].replace(0, pd.NA)
df["AE_12hr_Breach_Rate"] = df["Patients who have waited 12+ hrs from DTA to admission"] / df["A&E attendances Type 1"].replace(0, pd.NA)

# ============================
# 6. WORKFORCE FEATURES
# ============================

df["Workforce_Clinical"] = df["Medical"] + df["Nursing"]
df["Workforce_Clinical_Ratio"] = df["Workforce_Clinical"] / df["Total"].replace(0, pd.NA)
df["Workforce_Admin_Ratio"] = df["Admin"] / df["Total"].replace(0, pd.NA)

# ============================
# 7. NORMALISED SCORES (0–1)
# ============================

def normalise(series):
    return (series - series.min()) / (series.max() - series.min())

df["Norm_DMA"] = normalise(df["DMA_Average"])
df["Norm_RTT"] = 1 - normalise(df["RTT_Backlog_Ratio"])  # lower backlog = better
df["Norm_DM01"] = 1 - normalise(df["DM01_6Week_Rate"])
df["Norm_AE"] = 1 - normalise(df["AE_4hr_Breach_Rate"])
df["Norm_Workforce"] = normalise(df["Workforce_Clinical_Ratio"])

# ============================
# 8. EPR READINESS SCORE (0–100)
# ============================

df["EPR_Readiness"] = (
    0.40 * df["Norm_DMA"] +
    0.20 * df["Norm_RTT"] +
    0.15 * df["Norm_DM01"] +
    0.15 * df["Norm_AE"] +
    0.10 * df["Norm_Workforce"]
) * 100

# ============================
# Save engineered dataset
# ============================

df.to_csv("../data/processed/master_trust_dataset_engineered.csv", index=False)

print("Feature engineering complete!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print(df[["Org Code", "Org Name", "EPR_Readiness"]].head())
