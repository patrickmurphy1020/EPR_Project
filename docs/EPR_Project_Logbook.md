# 📘 Electronic Patient Record (EPR) Project Logbook
### *How EPR Usability and Digital Maturity Influence Clinical Decision‑Making at Leeds Teaching Hospitals NHS Trust*

---

## 1. Project Overview
**Aim:**  
Evaluate how improvements in EPR usability and digital maturity affect clinical decision‑making, operational performance, and patient safety.

**Trust Focus:**  
Leeds Teaching Hospitals NHS Trust (LTHT)

**Context:**  
West Yorkshire ICS + national NHS digital strategy

**Why This Matters:**  
EPR optimisation is a national priority. BI teams must measure its impact on decision‑making, performance, and safety.

---

## 2. Data Sources

### 2.1 Real NHS Datasets
- **Digital Maturity Assessment (DMA)**  
  - Overall maturity  
  - Data quality  
  - Interoperability  
  - Analytics capability  
  - Workforce digital skills  

- **EPR Usability Survey (2024)**  
  - Staff satisfaction  
  - Workflow integration  
  - Documentation time  
  - Ease of finding information  
  - Training adequacy  

- **NHS Performance Metrics**  
  - A&E 4‑hour performance  
  - Discharge delays  
  - Outpatient waits  
  - Diagnostic turnaround times  

- **NHS Staff Survey (Digital Questions)**  
  - Access to information  
  - Digital tools  
  - Training  
  - Workload  
  - Confidence in systems  

### 2.2 Simulated Datasets (Based on Real NHS Patterns)
- Duplicate test ordering  
- Medication error rates  
- Decision delays  
- Data completeness  
- Documentation time  
- Alert fatigue indicators  

**Note:** Simulated metrics reflect real NHS evidence, not random values.

---

## 3. Data Engineering Notes (Python)

### 3.1 Cleaning Steps
- Standardise trust codes  
- Handle missing values  
- Convert all scores to 0–100 scale  
- Normalise distributions where needed  

### 3.2 Dataset Joins
- Join on trust code (e.g., RTH, RXF)  
- Merge DMA + Usability + Staff Survey + Performance  

### 3.3 Feature Engineering
- **EPR Usability Score** (composite)  
- **Digital Maturity Composite Score**  
- **Performance Score**  
- **Decision Quality Index (DQI)**  

### 3.4 Decision Quality Index (DQI)
**Formula (0–100):**  
- Data completeness (20%)  
- Timeliness (20%)  
- Accuracy (20%)  
- Consistency (20%)  
- Error rate (20%)  

### 3.5 Predictive Modelling
Model: Linear Regression / Ridge Regression  
**Predict:**  
- Performance improvement  
- Error reduction  
- Decision delay reduction  

### 3.6 Export to Tableau
- Export final dataset as `analysis_ready.csv`  
- Include:  
  - Trust metadata  
  - DMA scores  
  - Usability scores  
  - Staff survey metrics  
  - Simulated decision‑making metrics  
  - Model predictions  

---

## 4. Tableau Dashboard Notes

### 4.1 Page 1 — Overview
- Digital maturity  
- EPR usability  
- DQI  
- Key performance indicators  
- High‑level insights  

### 4.2 Page 2 — Digital Maturity Deep Dive
- Radar chart of DMA sub‑scores  
- Benchmark vs ICS average  
- Trend (if available)  

### 4.3 Page 3 — EPR Usability & Staff Experience
- Staff satisfaction  
- Training completion  
- Workflow integration  
- Documentation time  

### 4.4 Page 4 — Decision‑Making & Performance
- Duplicate tests  
- Medication errors  
- Decision delays  
- Discharge delays  
- Diagnostic turnaround times  

### 4.5 Page 5 — What‑If Analysis Tool
**Inputs (sliders):**  
- EPR usability  
- Digital maturity  
- Training completion  

**Outputs:**  
- Predicted DQI  
- Predicted error rate  
- Predicted duplicate tests  
- Predicted discharge delays  

---

## 5. Decision Theory Notes

### 5.1 Biases Reduced by Good EPR Usability
- Availability bias  
- Anchoring  
- Omission bias  
- Confirmation bias  

### 5.2 Biases Introduced by Poor Usability
- Automation bias  
- Alert fatigue  
- Information overload  
- Default anchoring  

### 5.3 Frameworks Used
- Multi‑criteria decision analysis (MCDA)  
- Expected value of improved decisions  
- Risk analysis  
- Uncertainty modelling  

---

## 6. Insights & Findings (To Fill In Later)
- Key patterns  
- Relationships between maturity, usability, and performance  
- Predictive model results  
- What‑If tool insights  

---

## 7. Recommendations (BI‑Style)
- Improve EPR usability through workflow redesign  
- Targeted training for low‑adoption departments  
- Introduce new KPIs for decision quality  
- Improve interoperability between EPR and diagnostics  
- Use DMA scores to prioritise investment  

---

## 8. AI Usage Notes
- AI assisted with brainstorming and structuring  
- AI refined decision theory concepts  
- All data preparation, modelling, and dashboarding done manually  
- AI did not generate the dataset or final analysis  

---

## 9. Reflection (For Employers)
- What I learned  
- Tools used (Python, Tableau, NHS datasets)  
- Skills demonstrated  
- How this project reflects real BI work  

---
