import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
NUM_PATIENTS = 7500
OUTPUT_PATH = "../data/simulated/patients.csv"

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# -----------------------------
# 1. Generate Patient IDs
# -----------------------------
patient_ids = [f"P{str(i).zfill(5)}" for i in range(1, NUM_PATIENTS + 1)]

# -----------------------------
# 2. Age Distribution (Realistic NHS Shape)
# -----------------------------
age_groups = [
    (0, 17, 0.15),
    (18, 40, 0.25),
    (41, 65, 0.30),
    (66, 85, 0.25),
    (86, 95, 0.05)
]

ages = []
for low, high, weight in age_groups:
    count = int(NUM_PATIENTS * weight)
    ages.extend(np.random.randint(low, high + 1, count))

# Adjust length if rounding caused mismatch
ages = ages[:NUM_PATIENTS]

# -----------------------------
# 3. Gender Distribution
# -----------------------------
genders = np.random.choice(
    ["Female", "Male", "Other"],
    size=NUM_PATIENTS,
    p=[0.51, 0.48, 0.01]
)

# -----------------------------
# 4. Postcode Districts (Weighted by Deprivation)
# -----------------------------
postcode_weights = {
    "LS9": 0.15,   # more deprived
    "LS11": 0.15,  # more deprived
    "LS12": 0.10,  # more deprived
    "LS1": 0.10,
    "LS2": 0.10,
    "LS3": 0.05,
    "LS4": 0.05,
    "LS6": 0.10,
    "LS7": 0.10,
    "LS8": 0.10
}

postcodes = np.random.choice(
    list(postcode_weights.keys()),
    size=NUM_PATIENTS,
    p=list(postcode_weights.values())
)

# -----------------------------
# 5. Registration Dates (2015–2024)
# -----------------------------
start_date = datetime(2015, 1, 1)
end_date = datetime(2024, 12, 31)

def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

registration_dates = [random_date(start_date, end_date) for _ in range(NUM_PATIENTS)]

# -----------------------------
# 6. Build DataFrame
# -----------------------------
df_patients = pd.DataFrame({
    "PatientID": patient_ids,
    "Age": ages,
    "Gender": genders,
    "PostcodeDistrict": postcodes,
    "RegistrationDate": registration_dates
})

# -----------------------------
# 7. Save to CSV
# -----------------------------
df_patients.to_csv(OUTPUT_PATH, index=False)

print(f"Patients table created with {NUM_PATIENTS} rows → {OUTPUT_PATH}")


# ============================================================
#  APPOINTMENTS TABLE SIMULATION
# ============================================================

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Load patients table
patients_df = pd.read_csv("../data/simulated/patients.csv")

# -----------------------------
# CONFIGURATION
# -----------------------------
OUTPUT_PATH_APPTS = "../data/simulated/appointments.csv"

# Ensure directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH_APPTS), exist_ok=True)

# -----------------------------
# 1. Generate number of appointments per patient
# -----------------------------
def appointments_per_patient(age):
    """Realistic NHS logic: older patients have more appointments."""
    if age < 18:
        return np.random.poisson(2)   # children: fewer
    elif age < 40:
        return np.random.poisson(3)
    elif age < 65:
        return np.random.poisson(4)
    else:
        return np.random.poisson(6)   # older adults: more

appointments_list = []

# -----------------------------
# 2. Generate appointments
# -----------------------------
for _, row in patients_df.iterrows():
    patient_id = row["PatientID"]
    age = row["Age"]
    postcode = row["PostcodeDistrict"]

    num_appts = max(1, appointments_per_patient(age))

    for _ in range(num_appts):
        # Booking date
        booking_date = datetime(
            np.random.randint(2018, 2025),
            np.random.randint(1, 13),
            np.random.randint(1, 28)
        )

        # Wait time logic (Before vs After EPR)
        if booking_date.year < 2022:
            wait_days = int(np.random.normal(42, 10))  # longer waits
            epr_period = "BeforeEPR"
        else:
            wait_days = int(np.random.normal(28, 7))   # improved waits
            epr_period = "AfterEPR"

        wait_days = max(1, wait_days)
        appointment_date = booking_date + timedelta(days=wait_days)

        # DNA logic
        base_dna = 0.07  # 7% baseline

        # deprivation effect
        if postcode in ["LS9", "LS11", "LS12"]:
            base_dna += 0.04

        # age effect
        if 18 <= age <= 30:
            base_dna += 0.05
        if age >= 65:
            base_dna -= 0.03

        # EPR improvement
        if epr_period == "AfterEPR":
            base_dna -= 0.02

        base_dna = max(0.01, min(base_dna, 0.25))  # clamp between 1% and 25%

        status = np.random.choice(
            ["Completed", "DNA", "Cancelled"],
            p=[1 - base_dna - 0.03, base_dna, 0.03]
        )

        # Duration
        duration = np.random.choice([15, 20, 30], p=[0.4, 0.4, 0.2])

        appointments_list.append([
            f"A{random.randint(100000, 999999)}",
            patient_id,
            booking_date,
            appointment_date,
            random.choice(["Cardiology", "Dermatology", "Orthopaedics", "ENT", "General Medicine"]),
            status,
            duration,
            epr_period
        ])

# -----------------------------
# 3. Build DataFrame
# -----------------------------
appointments_df = pd.DataFrame(appointments_list, columns=[
    "AppointmentID",
    "PatientID",
    "BookingDate",
    "AppointmentDate",
    "Department",
    "Status",
    "DurationMinutes",
    "EPRPeriod"
])

# -----------------------------
# 4. Save to CSV
# -----------------------------
appointments_df.to_csv(OUTPUT_PATH_APPTS, index=False)

print(f"Appointments table created with {len(appointments_df)} rows → {OUTPUT_PATH_APPTS}")


# ============================================================
#  MEDICATION ERRORS TABLE SIMULATION
# ============================================================

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Load patients table
patients_df = pd.read_csv("../data/simulated/patients.csv")

# -----------------------------
# CONFIGURATION
# -----------------------------
OUTPUT_PATH_ERRORS = "../data/simulated/medication_errors.csv"

# Ensure directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH_ERRORS), exist_ok=True)

# -----------------------------
# 1. Error rate assumptions
# -----------------------------
# NHS studies show ~20–40% reduction after EPR
ERROR_RATE_BEFORE = 6.2 / 1000   # per patient
ERROR_RATE_AFTER = 4.1 / 1000    # per patient

# Severity distribution (realistic NHS pattern)
severity_weights = {
    "Low": 0.70,
    "Medium": 0.25,
    "High": 0.05
}

error_types = [
    "Wrong Dose",
    "Wrong Patient",
    "Omission",
    "Allergy Missed",
    "Transcription Error"
]

# -----------------------------
# 2. Generate errors
# -----------------------------
errors_list = []

for _, row in patients_df.iterrows():
    patient_id = row["PatientID"]
    age = row["Age"]

    # Determine EPR period based on registration date
    # (Patients registered before 2022 have both periods)
    if row["RegistrationDate"] < "2022-01-01":
        periods = ["BeforeEPR", "AfterEPR"]
    else:
        periods = ["AfterEPR"]

    for period in periods:
        # Determine number of errors for this patient in this period
        if period == "BeforeEPR":
            num_errors = np.random.poisson(ERROR_RATE_BEFORE)
        else:
            num_errors = np.random.poisson(ERROR_RATE_AFTER)

        for _ in range(num_errors):
            # Random date in the correct period
            if period == "BeforeEPR":
                year = np.random.randint(2018, 2022)
            else:
                year = np.random.randint(2022, 2025)

            date = datetime(
                year,
                np.random.randint(1, 13),
                np.random.randint(1, 28)
            )

            errors_list.append([
                f"E{random.randint(100000, 999999)}",
                patient_id,
                random.choice(error_types),
                np.random.choice(list(severity_weights.keys()), p=list(severity_weights.values())),
                date,
                period
            ])

# -----------------------------
# 3. Build DataFrame
# -----------------------------
errors_df = pd.DataFrame(errors_list, columns=[
    "ErrorID",
    "PatientID",
    "ErrorType",
    "Severity",
    "Date",
    "EPRPeriod"
])

# -----------------------------
# 4. Save to CSV
# -----------------------------
errors_df.to_csv(OUTPUT_PATH_ERRORS, index=False)

print(f"MedicationErrors table created with {len(errors_df)} rows → {OUTPUT_PATH_ERRORS}")


# ============================================================
#  DUPLICATE TESTS TABLE SIMULATION
# ============================================================

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Load patients table
patients_df = pd.read_csv("../data/simulated/patients.csv")

# -----------------------------
# CONFIGURATION
# -----------------------------
OUTPUT_PATH_DUP = "../data/simulated/duplicate_tests.csv"

# Ensure directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH_DUP), exist_ok=True)

# -----------------------------
# 1. Duplicate test rate assumptions
# -----------------------------
# NHS studies show EPR reduces duplicate tests by ~20–30%
DUP_RATE_BEFORE = 0.045   # 4.5% of patients
DUP_RATE_AFTER = 0.028    # 2.8% of patients

test_types = {
    "Blood Test": 0.50,
    "Imaging": 0.30,
    "Microbiology": 0.20
}

duplicate_tests_list = []

# -----------------------------
# 2. Generate duplicate tests
# -----------------------------
for _, row in patients_df.iterrows():
    patient_id = row["PatientID"]

    # Determine EPR periods for this patient
    if row["RegistrationDate"] < "2022-01-01":
        periods = ["BeforeEPR", "AfterEPR"]
    else:
        periods = ["AfterEPR"]

    for period in periods:
        # Determine number of duplicate tests
        if period == "BeforeEPR":
            num_tests = np.random.poisson(DUP_RATE_BEFORE)
        else:
            num_tests = np.random.poisson(DUP_RATE_AFTER)

        for _ in range(num_tests):
            # Random date in correct period
            if period == "BeforeEPR":
                year = np.random.randint(2018, 2022)
            else:
                year = np.random.randint(2022, 2025)

            date = datetime(
                year,
                np.random.randint(1, 13),
                np.random.randint(1, 28)
            )

            duplicate_tests_list.append([
                f"T{random.randint(100000, 999999)}",
                patient_id,
                np.random.choice(list(test_types.keys()), p=list(test_types.values())),
                date,
                "Duplicate",
                period
            ])

# -----------------------------
# 3. Build DataFrame
# -----------------------------
duplicate_df = pd.DataFrame(duplicate_tests_list, columns=[
    "TestID",
    "PatientID",
    "TestType",
    "Date",
    "Reason",
    "EPRPeriod"
])

# -----------------------------
# 4. Save to CSV
# -----------------------------
duplicate_df.to_csv(OUTPUT_PATH_DUP, index=False)

print(f"DuplicateTests table created with {len(duplicate_df)} rows → {OUTPUT_PATH_DUP}")


# ============================================================
#  STAFF WORKFLOW TABLE SIMULATION
# ============================================================

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
OUTPUT_PATH_WORKFLOW = "../data/simulated/staff_workflow.csv"

# Ensure directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH_WORKFLOW), exist_ok=True)

# -----------------------------
# 1. Workflow assumptions
# -----------------------------
roles = ["Nurse", "Doctor", "Admin"]

tasks = {
    "Documentation": {"Before": 12, "After": 7},
    "Ordering Tests": {"Before": 6, "After": 3},
    "Updating Notes": {"Before": 5, "After": 3},
    "Discharge Summary": {"Before": 15, "After": 10}
}

# Number of workflow samples to generate
NUM_WORKFLOW_ROWS = 10000

workflow_rows = []

# -----------------------------
# 2. Generate workflow measurements
# -----------------------------
for _ in range(NUM_WORKFLOW_ROWS):

    role = random.choice(roles)
    task = random.choice(list(tasks.keys()))

    # Randomly assign Before/After EPR period
    period = np.random.choice(["BeforeEPR", "AfterEPR"], p=[0.45, 0.55])

    # Select mean time based on period
    if period == "BeforeEPR":
        mean_time = tasks[task]["Before"]
        year = np.random.randint(2018, 2022)
    else:
        mean_time = tasks[task]["After"]
        year = np.random.randint(2022, 2025)

    # Generate realistic time with slight variation
    time_taken = max(1, int(np.random.normal(mean_time, mean_time * 0.15)))

    # Random date
    date = datetime(
        year,
        np.random.randint(1, 13),
        np.random.randint(1, 28)
    )

    workflow_rows.append([
        f"W{random.randint(100000, 999999)}",
        role,
        task,
        time_taken,
        date,
        period
    ])

# -----------------------------
# 3. Build DataFrame
# -----------------------------
workflow_df = pd.DataFrame(workflow_rows, columns=[
    "WorkflowID",
    "StaffRole",
    "TaskName",
    "TimeMinutes",
    "Date",
    "EPRPeriod"
])

# -----------------------------
# 4. Save to CSV
# -----------------------------
workflow_df.to_csv(OUTPUT_PATH_WORKFLOW, index=False)

print(f"StaffWorkflow table created with {len(workflow_df)} rows → {OUTPUT_PATH_WORKFLOW}")
