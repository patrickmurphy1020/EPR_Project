import pandas as pd
import os

# ============================================================
#  EXPORT CLEAN TABLES FOR TABLEAU
# ============================================================

# Ensure output folder exists
os.makedirs("../tableau", exist_ok=True)

# -----------------------------
# 1. Load processed datasets
# -----------------------------
patients = pd.read_csv("../data/processed/patients_clean.csv")
appointments = pd.read_csv("../data/processed/appointments_clean.csv")
med_errors = pd.read_csv("../data/processed/medication_errors_clean.csv")
dup_tests = pd.read_csv("../data/processed/duplicate_tests_clean.csv")
workflow = pd.read_csv("../data/processed/staff_workflow_clean.csv")
fact_appointments = pd.read_csv("../data/processed/fact_appointments.csv")

# -----------------------------
# 2. Export to Tableau folder
# -----------------------------
patients.to_csv("../tableau/patients.csv", index=False)
appointments.to_csv("../tableau/appointments.csv", index=False)
med_errors.to_csv("../tableau/medication_errors.csv", index=False)
dup_tests.to_csv("../tableau/duplicate_tests.csv", index=False)
workflow.to_csv("../tableau/staff_workflow.csv", index=False)
fact_appointments.to_csv("../tableau/fact_appointments.csv", index=False)

print("All datasets exported to /tableau/ for Tableau use.")
