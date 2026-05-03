# 📘 Evaluating the Impact of Electronic Patient Record (EPR) Implementation at Leeds Teaching Hospitals NHS Trust

A data analytics project assessing how Electronic Patient Record (EPR) implementation influences operational performance, efficiency, safety, and decision‑making within an NHS trust.  
The analysis combines real NHS datasets with simulated patient‑level metrics to model before‑and‑after changes in key performance indicators.

This project is designed to reflect the type of analytical work carried out by NHS Business Intelligence teams.

---

## 🎯 Project Purpose

NHS trusts increasingly rely on EPR systems to improve:

- clinical documentation  
- workflow efficiency  
- patient safety  
- data quality  
- operational decision‑making  

However, patient‑level data is not publicly available.  
To overcome this, the project uses:

- **Real NHS trust‑level datasets** (Digital Maturity, performance reports, ICS context)  
- **Simulated patient‑level data** (appointments, DNAs, wait times, medication errors, workflow metrics)  

This allows a realistic evaluation of how EPR adoption affects measurable outcomes.

---

## 🧱 Tech Stack

| Layer | Tools |
|------|-------|
| **Data Sources** | NHS Digital, NHS England, LTHT reports, simulated datasets |
| **Data Processing** | Python (pandas, numpy) |
| **Data Modelling** | Python, CSV exports |
| **Visualisation** | Tableau |
| **Documentation** | Markdown (VS Code) |
| **Version Control** | Git & GitHub |

---

## 🏥 Project Scope

### **1. Trust Selection**
Leeds Teaching Hospitals NHS Trust (LTHT), with ICS‑level context from West Yorkshire.

### **2. Real NHS Data Used**
- NHS Digital Maturity Assessment  
- EPR usability and adoption indicators  
- Trust‑level performance metrics  
- ICS and national benchmarks  

### **3. Simulated Data (Patient‑Level)**
To model before/after EPR impact:
- Appointment volumes  
- DNA rates  
- Waiting times  
- Duplicate tests  
- Medication errors  
- Staff adoption metrics  
- Workflow timings  

### **4. Analytical Focus**
- Efficiency improvements  
- Safety improvements  
- Data quality changes  
- Operational KPIs  
- Decision‑making enhancements  

---

## 📊 Planned KPIs

### **Efficiency**
- DNA rate  
- Average wait time  
- Appointment throughput  
- Time per clinical documentation task  

### **Safety**
- Medication error rate  
- Duplicate test rate  
- Missing/incorrect documentation incidents  

### **Data Quality**
- Completeness of records  
- Timeliness of updates  
- Reduction in manual entry  

### **Decision‑Making**
- KPI availability  
- Reporting latency  
- Data‑driven operational insights  

---

## 🧪 Python Workflow

```
python/
│
├── 01_data_cleaning.py
├── 02_feature_engineering.py
├── 03_simulation.py
├── 04_modelling.py
└── 05_export_for_tableau.py
```

Each script represents a stage in the analytical pipeline:

1. Clean real NHS datasets  
2. Generate simulated patient‑level data  
3. Create before/after EPR scenarios  
4. Model KPIs and performance changes  
5. Export datasets for Tableau  

---

## 🎨 Tableau Dashboard (Planned)

The dashboard will visualise:

- Before vs after EPR KPIs  
- Efficiency and safety improvements  
- Trust vs ICS vs national benchmarks  
- Patient‑level simulated insights  
- Operational decision‑making metrics  

---

## 📂 Project Structure

```
EPR_Impact_Project/
│
├── data/
│   ├── real/               # Real NHS datasets
│   └── simulated/          # Patient-level simulated data
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
```

---

## 📝 Project Logbook

All development notes, decisions, and progress are documented in:

```
docs/EPR_Project_Logbook.md
```

---


