# 📘 Dataset Schema for EPR Impact Analysis

This schema defines the structure of all datasets used in the project.  
It includes real NHS datasets and simulated patient‑level datasets, along with the relationships and KPIs they support.

---

# 1. Real NHS Datasets (Trust‑Level)

These datasets provide context for LTHT’s digital maturity, performance, and regional benchmarks.

## 1.1 Digital Maturity Assessment
**Source:** NHS England  
**Grain:** Trust-level  
**Purpose:** Establish baseline EPR readiness and adoption

| Field | Description |
|-------|-------------|
| TrustCode | LTHT code |
| TrustName | Leeds Teaching Hospitals NHS Trust |
| EPRScore | Digital maturity score for EPR |
| LeadershipScore | Digital leadership maturity |
| InfrastructureScore | Technical readiness |
| Year | Reporting year |

---

## 1.2 ICS Benchmark Data
**Source:** NHS England  
**Grain:** ICS-level  
**Purpose:** Compare LTHT to West Yorkshire ICS and national averages

| Field | Description |
|-------|-------------|
| ICSName | West Yorkshire ICS |
| MetricName | e.g., “Digital Maturity”, “EPR Adoption” |
| MetricValue | Score or percentage |
| Year | Reporting year |

---

## 1.3 Trust Performance Metrics
**Source:** LTHT public reports  
**Grain:** Trust-level  
**Purpose:** Provide real operational context

| Field | Description |
|-------|-------------|
| Month | Reporting month |
| AandEWaits4hr | % seen within 4 hours |
| RTT18Weeks | % within 18 weeks |
| DNARate | Trust-level DNA rate |
| BedOccupancy | % occupancy |
| CancelledOps | Number cancelled |

---

# 2. Simulated Patient‑Level Datasets

These datasets model before/after EPR changes.  
They are realistic but contain **no real patient data**.

---

## 2.1 Patients Table
**Grain:** One row per patient  
**Purpose:** Demographics for segmentation

| Field | Description |
|-------|-------------|
| PatientID | Unique ID |
| Age | Age at time of appointment |
| Gender | M/F/Other |
| Postcode | Used for deprivation index |
| RegistrationDate | When patient joined LTHT |

---

## 2.2 Appointments Table
**Grain:** One row per appointment  
**Purpose:** DNA rate, throughput, wait times

| Field | Description |
|-------|-------------|
| AppointmentID | Unique ID |
| PatientID | Links to Patients |
| BookingDate | When appointment was booked |
| AppointmentDate | Scheduled date |
| Department | Clinic/service |
| Status | Completed / DNA / Cancelled |
| DurationMinutes | Length of appointment |
| EPRPeriod | BeforeEPR / AfterEPR |

**KPIs supported:**  
- DNA rate  
- Average wait time  
- Appointment throughput  

---

## 2.3 MedicationErrors Table
**Grain:** One row per error event  
**Purpose:** Safety KPI

| Field | Description |
|-------|-------------|
| ErrorID | Unique ID |
| PatientID | Links to Patients |
| ErrorType | Wrong dose / wrong patient / omission |
| Severity | Low / Medium / High |
| Date | When error occurred |
| EPRPeriod | BeforeEPR / AfterEPR |

**KPIs supported:**  
- Medication error rate  
- Severity distribution  

---

## 2.4 DuplicateTests Table
**Grain:** One row per duplicate diagnostic test  
**Purpose:** Efficiency + safety

| Field | Description |
|-------|-------------|
| TestID | Unique ID |
| PatientID | Links to Patients |
| TestType | Bloods / Imaging / etc |
| Date | When test occurred |
| Reason | Duplicate / unnecessary |
| EPRPeriod | BeforeEPR / AfterEPR |

**KPIs supported:**  
- Duplicate test rate  

---

## 2.5 StaffWorkflow Table
**Grain:** One row per workflow measurement  
**Purpose:** Time savings from EPR

| Field | Description |
|-------|-------------|
| WorkflowID | Unique ID |
| StaffRole | Nurse / Doctor / Admin |
| TaskName | Documentation / Ordering tests / etc |
| TimeMinutes | Time taken |
| EPRPeriod | BeforeEPR / AfterEPR |

**KPIs supported:**  
- Time per documentation task  
- Workflow efficiency  

---

# 3. Relationships (Data Model)

```
Patients (1) ──── (∞) Appointments
Patients (1) ──── (∞) MedicationErrors
Patients (1) ──── (∞) DuplicateTests
```

Trust-level datasets sit **above** patient-level data and do not link directly.

---

# 4. KPI Definitions

## Efficiency KPIs
- **DNA Rate** = DNAs / Total Appointments  
- **Average Wait Time** = AppointmentDate – BookingDate  
- **Appointment Throughput** = Completed Appointments per Month  
- **Documentation Time Reduction** = AvgBefore – AvgAfter  

## Safety KPIs
- **Medication Error Rate** = Errors / 1000 Patients  
- **Duplicate Test Rate** = DuplicateTests / TotalTests  

## Data Quality KPIs
- **Record Completeness** = % of fields populated  
- **Timeliness** = Time between event and record entry  

## Decision‑Making KPIs
- **Reporting Latency** = Time from month-end to KPI availability  
- **Data Availability Score** = % KPIs available on time  

---

# 5. Real vs Simulated Summary

| Table | Real or Simulated | Reason |
|-------|-------------------|--------|
| Digital Maturity | Real | Public NHS dataset |
| ICS Benchmarks | Real | Public NHS dataset |
| Trust Performance | Real | Public LTHT data |
| Patients | Simulated | Patient-level data is private |
| Appointments | Simulated | Needed for KPIs |
| MedicationErrors | Simulated | Not publicly available |
| DuplicateTests | Simulated | Not publicly available |
| StaffWorkflow | Simulated | Not publicly available |

---

# 6. Purpose of This Schema

This schema ensures:

- The project is **focused**  
- You only collect the data you need  
- Your Python scripts have a clear structure  
- Your Tableau dashboard has a clean data model  
- Your repo looks like a **real NHS BI project**  

