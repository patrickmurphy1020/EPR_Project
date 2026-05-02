# EPR_Project
📘 EPR (Electronic Patient Record) Simulation & Analytics Project
A full end‑to‑end data analytics project simulating an Electronic Patient Record (EPR) system.
This project demonstrates professional BI workflow: data design, Python processing, simulation, modelling, and Tableau dashboarding — all version‑controlled in GitHub.
🚀 Project Overview
This project simulates a simplified EPR system to explore:
How patient, appointment, and clinical data can be structured
How raw data can be cleaned, transformed, and modelled
How KPIs can be generated for operational insights
How a BI developer documents and manages a real project
The goal is to produce a portfolio‑ready analytics project that demonstrates:
Data engineering fundamentals
Python data processing
Data modelling
Dashboard design
Professional documentation
Git/GitHub version control
🧱 Tech Stack
Layer	Tools
Data Processing	Python (pandas, numpy)
Data Modelling	Python, CSV exports
Visualisation	Tableau
Documentation	Markdown (VS Code)
Version Control	Git & GitHub


📂 Project Structure
Code
EPR_Project/
│
├── data/
│   ├── raw/                # Raw simulated data (ignored by Git)
│   └── processed/          # Cleaned & modelled data for Tableau
│
├── python/
│   ├── 01_data_cleaning.py
│   ├── 02_feature_engineering.py
│   ├── 03_simulation.py
│   ├── 04_modelling.py
│   └── 05_export_for_tableau.py
│
├── docs/
│   ├── EPR_Project_Logbook.md
│   └── tableau_notes.md
│
├── .gitignore
└── README.md
🏥 Dataset Description
The project simulates the following core tables:
1. Patients
PatientID
Name
DOB
Gender
RegistrationDate
2. Appointments
AppointmentID
PatientID
AppointmentDate
Department
Status (Completed / DNA / Cancelled)
3. Clinical Notes
NoteID
PatientID
Clinician
NoteDate
Summary
4. Medications
MedicationID
PatientID
DrugName
StartDate
EndDate
A full data dictionary will be included in the /docs folder.
📊 Planned KPIs
DNA rate
Appointment volume by department
Average wait time
Active patients
Medication counts
Patient demographics
🎨 Tableau Dashboard (Planned)
The final dashboard will include:
KPI summary tiles
Appointment trends
Department performance
Patient demographics
Medication insights
Design notes are tracked in docs/tableau_notes.md.
🧪 Python Pipeline
Each script in /python represents a stage in the data workflow:
Data Cleaning
Feature Engineering
Simulation Logic
Modelling & KPI generation
Export to Tableau
📝 Project Logbook
All development notes, decisions, and progress are documented in:
Code
docs/EPR_Project_Logbook.md
This acts as a professional project diary.
🎯 Project Goals
Build a realistic EPR simulation dataset
Demonstrate BI developer workflow
Produce a clean, professional GitHub portfolio project
Showcase Python + Tableau + documentation skills
Practice version control and project structure
📌 Status
Current Phase: Repository setup & documentation
Next Phase: Dataset schema design