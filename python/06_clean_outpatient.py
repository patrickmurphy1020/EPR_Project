import pandas as pd

# Input and output paths
input_path = "../data/real/nhs/outpatient_activity.csv"
output_path = "../data/processed/outpatient_activity_clean.csv"

# Load CSV
df = pd.read_csv(input_path)

# ============================================================
# 1. FILTER TO PROVIDER LEVEL ONLY
# ============================================================
df = df[df["GEOGRAPHY_LEVEL"] == "03.Provider"]

# ============================================================
# 2. KEEP ONLY ANNUAL TOTALS
#    (REPORTING_PERIOD = 2425 for 2024–25)
# ============================================================
df = df[df["REPORTING_PERIOD"] == 2425]

# ============================================================
# 3. SELECT ONLY THE MEASURES WE CARE ABOUT
# ============================================================
keep_measures = [
    "01.Attended-Female",
    "02.Attended-Male",
    "03.Attended-Unknown Gender",
    "04.DNA-Female",
    "05.DNA-Male",
    "06.DNA-Unknown Gender",
    "07.Patient Cancelled-Female",
    "08.Patient Cancelled-Male",
    "09.Patient Cancelled-Unknown Gender",
    "10.Provider Cancelled-Female",
    "11.Provider Cancelled-Male",
    "12.Provider Cancelled-Unknown Gender",
    "13.Total Attendances"
]

df = df[df["MEASURE"].isin(keep_measures)]

# ============================================================
# 4. PIVOT INTO WIDE FORMAT
# ============================================================
df_pivot = df.pivot_table(
    index=["ORGANISATION_CODE", "ORGANISATION_DESCRIPTION"],
    columns="MEASURE",
    values="MEASURE_VALUE",
    aggfunc="sum"
).reset_index()

# ============================================================
# 5. RENAME COLUMNS FOR CLEAN MODELING
# ============================================================
df_pivot = df_pivot.rename(columns={
    "ORGANISATION_CODE": "TrustCode",
    "ORGANISATION_DESCRIPTION": "TrustName",
    "01.Attended-Female": "Attended_Female",
    "02.Attended-Male": "Attended_Male",
    "03.Attended-Unknown Gender": "Attended_Unknown",
    "04.DNA-Female": "DNA_Female",
    "05.DNA-Male": "DNA_Male",
    "06.DNA-Unknown Gender": "DNA_Unknown",
    "07.Patient Cancelled-Female": "CancelledByPatient_Female",
    "08.Patient Cancelled-Male": "CancelledByPatient_Male",
    "09.Patient Cancelled-Unknown Gender": "CancelledByPatient_Unknown",
    "10.Provider Cancelled-Female": "CancelledByProvider_Female",
    "11.Provider Cancelled-Male": "CancelledByProvider_Male",
    "12.Provider Cancelled-Unknown Gender": "CancelledByProvider_Unknown",
    "13.Total Attendances": "Total_Attendances"
})

# ============================================================
# 6. SAVE CLEANED OUTPUT
# ============================================================
df_pivot.to_csv(output_path, index=False)

print("Outpatient dataset cleaned and saved to:", output_path)
