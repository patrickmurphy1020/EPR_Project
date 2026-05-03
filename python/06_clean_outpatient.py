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
# 2. KEEP ONLY ANNUAL TOTALS (2024–25)
# ============================================================
df = df[df["REPORTING_PERIOD"] == 2425]

# ============================================================
# 3. KEEP ONLY MEASURE_TYPE = "Attendance Summary by Gender"
# ============================================================
df = df[df["MEASURE_TYPE"] == "Attendance Summary by Gender"]

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
# 5. RENAME COLUMNS
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
    "07.Patient Cancelled-Female": "Cancelled_Patient_Female",
    "08.Patient Cancelled-Male": "Cancelled_Patient_Male",
    "09.Patient Cancelled-Unknown Gender": "Cancelled_Patient_Unknown",
    "10.Hospital Cancelled-Female": "Cancelled_Hospital_Female",
    "11.Hospital Cancelled-Male": "Cancelled_Hospital_Male",
    "12.Hospital Cancelled-Unknown Gender": "Cancelled_Hospital_Unknown"
})

# ============================================================
# 6. CONVERT ALL MEASURES TO NUMERIC
# ============================================================
measure_cols = [
    "Attended_Female", "Attended_Male", "Attended_Unknown",
    "DNA_Female", "DNA_Male", "DNA_Unknown",
    "Cancelled_Patient_Female", "Cancelled_Patient_Male", "Cancelled_Patient_Unknown",
    "Cancelled_Hospital_Female", "Cancelled_Hospital_Male", "Cancelled_Hospital_Unknown"
]

for col in measure_cols:
    if col in df_pivot.columns:
        df_pivot[col] = pd.to_numeric(df_pivot[col], errors="coerce").fillna(0)

# ============================================================
# 7. CREATE TOTALS (OPTION A)
# ============================================================
df_pivot["Total_Attended"] = (
    df_pivot["Attended_Female"] +
    df_pivot["Attended_Male"] +
    df_pivot["Attended_Unknown"]
)

df_pivot["Total_DNA"] = (
    df_pivot["DNA_Female"] +
    df_pivot["DNA_Male"] +
    df_pivot["DNA_Unknown"]
)

df_pivot["Total_Cancelled_Patient"] = (
    df_pivot["Cancelled_Patient_Female"] +
    df_pivot["Cancelled_Patient_Male"] +
    df_pivot["Cancelled_Patient_Unknown"]
)

df_pivot["Total_Cancelled_Hospital"] = (
    df_pivot["Cancelled_Hospital_Female"] +
    df_pivot["Cancelled_Hospital_Male"] +
    df_pivot["Cancelled_Hospital_Unknown"]
)

df_pivot["Total_Appointments"] = (
    df_pivot["Total_Attended"] +
    df_pivot["Total_DNA"] +
    df_pivot["Total_Cancelled_Patient"] +
    df_pivot["Total_Cancelled_Hospital"]
)

# ============================================================
# 8. FILTER TO ACUTE NHS TRUSTS ONLY
#    Trust ODS codes are always 3 characters and start with 'R'
# ============================================================
df_final = df_pivot[df_pivot["TrustCode"].str.match(r"^R[A-Z0-9]{2}$")]

# ============================================================
# 9. KEEP ONLY THE FINAL TOTALS
# ============================================================
df_final = df_final[[
    "TrustCode",
    "TrustName",
    "Total_Attended",
    "Total_DNA",
    "Total_Cancelled_Patient",
    "Total_Cancelled_Hospital",
    "Total_Appointments"
]]

# ============================================================
# 10. SAVE CLEANED OUTPUT
# ============================================================
df_final.to_csv(output_path, index=False)

print("Outpatient dataset cleaned and saved to:", output_path)
