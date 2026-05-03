import pandas as pd
import numpy as np
import os

# ============================================================
#  DATA PREPARATION PIPELINE
# ============================================================

# -----------------------------
# 1. Load simulated datasets
# -----------------------------
patients = pd.read_csv("../data/simulated/patients.csv")
appointments = pd.read_csv("../data/simulated/appointments.csv")
med_errors = pd.read_csv("../data/simulated/medication_errors.csv")
dup_tests = pd.read_csv("../data/simulated/duplicate_tests.csv")
workflow = pd.read_csv("../data/simulated/staff_workflow.csv")

# Ensure processed folder exists
os.makedirs("../data/processed", exist_ok=True)

# -----------------------------
# 2. Convert date fields
# -----------------------------
date_cols = {
    "patients": ["RegistrationDate"],
    "appointments": ["BookingDate", "AppointmentDate"],
    "med_errors": ["Date"],
    "dup_tests": ["Date"],
    "workflow": ["Date"]
}

patients["RegistrationDate"] = pd.to_datetime(patients["RegistrationDate"])
appointments["BookingDate"] = pd.to_datetime(appointments["BookingDate"])
appointments["AppointmentDate"] = pd.to_datetime(appointments["AppointmentDate"])
med_errors["Date"] = pd.to_datetime(med_errors["Date"])
dup_tests["Date"] = pd.to_datetime(dup_tests["Date"])
workflow["Date"] = pd.to_datetime(workflow["Date"])

# -----------------------------
# 3. Derived fields
# -----------------------------

# Age bands
def age_band(age):
    if age <= 17: return "0-17"
    if age <= 40: return "18-40"
    if age <= 65: return "41-65"
    if age <= 85: return "66-85"
    return "85+"

patients["AgeBand"] = patients["Age"].apply(age_band)

# Deprivation groups (based on postcode district)
deprived = ["LS9", "LS11", "LS12"]
patients["DeprivationGroup"] = patients["PostcodeDistrict"].apply(
    lambda x: "High Deprivation" if x in deprived else "Lower Deprivation"
)

# Appointment wait time
appointments["WaitDays"] = (appointments["AppointmentDate"] - appointments["BookingDate"]).dt.days
appointments["WaitDays"] = appointments["WaitDays"].clip(lower=0)

# DNA flag
appointments["DNAFlag"] = appointments["Status"].apply(lambda x: 1 if x == "DNA" else 0)

# Year fields for trend charts
appointments["Year"] = appointments["AppointmentDate"].dt.year
med_errors["Year"] = med_errors["Date"].dt.year
dup_tests["Year"] = dup_tests["Date"].dt.year
workflow["Year"] = workflow["Date"].dt.year

# -----------------------------
# 4. Join Appointments → Patients
# -----------------------------
fact_appointments = appointments.merge(
    patients,
    on="PatientID",
    how="left"
)

# -----------------------------
# 5. Export cleaned datasets
# -----------------------------
patients.to_csv("../data/processed/patients_clean.csv", index=False)
appointments.to_csv("../data/processed/appointments_clean.csv", index=False)
med_errors.to_csv("../data/processed/medication_errors_clean.csv", index=False)
dup_tests.to_csv("../data/processed/duplicate_tests_clean.csv", index=False)
workflow.to_csv("../data/processed/staff_workflow_clean.csv", index=False)

# Export main fact table
fact_appointments.to_csv("../data/processed/fact_appointments.csv", index=False)

print("Data preparation complete. Cleaned tables saved to /data/processed/")
