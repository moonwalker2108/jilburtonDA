<div align="center">

<h1>📄 Medicare Claims & Denials Analysis</h1>
<h3>SQL | Tableau | Healthcare Analytics</h3>

</div>

---

## 🧾 Business Problem

Healthcare providers rely on timely claim reimbursements to maintain revenue cycle stability. However, high denial rates can significantly delay payments, increase administrative costs, and reduce overall profitability.

The objective of this analysis was to identify:
- Key drivers of Medicare claim denials  
- Trends in denial rates over time  
- Areas of revenue leakage within the claims process  

---

## 📊 Data Overview

This analysis was conducted using a dataset of **400,000 Medicare Part B claims** (PHI-stripped), including:

- Claim submission and payment status  
- Denial reason codes  
- Provider-level performance  
- Monthly claim trends and reimbursement amounts  

Data was queried and transformed using SQL and visualized in Tableau to uncover patterns and performance gaps.

---

## 🔍 Key Insights

### 1. Denial Rates Are Increasing Over Time
- Denial rates increased approximately **18% year-over-year**  
- Spikes in denials aligned with periods of high claim volume, suggesting operational strain  

---

### 2. Documentation Issues Drive the Majority of Denials
- Missing or incomplete documentation accounted for **~32% of denials**  
- Coding errors and eligibility issues were the next most frequent causes  

---

### 3. Provider Performance Varies Significantly
- Some providers had denial rates **2x higher than average**  
- High-denial providers were linked to recurring documentation and coding issues  

---

### 4. Revenue Loss Is Concentrated in Key Areas
- A small subset of denial reasons drove the majority of revenue loss  
- High-cost procedures had disproportionately high denial rates  

---

## 💡 Recommendations

### ✔ Implement Pre-Submission Validation
- Introduce automated checks for documentation completeness and coding accuracy  
- Reduce preventable denials before submission  

---

### ✔ Target High-Risk Providers
- Provide focused training for providers with elevated denial rates  
- Monitor performance trends and enforce accountability  

---

### ✔ Standardize Documentation Processes
- Establish clear documentation guidelines across teams  
- Reduce variability in claim submissions  

---

### ✔ Monitor Denial Trends with Real-Time Dashboards
- Enable continuous tracking of denial metrics  
- Support faster response to emerging issues  

---

## 📈 Business Impact

If implemented, these improvements could:

- Reduce denial rates by **10–15%**  
- Recover significant lost revenue annually  
- Improve cash flow through faster reimbursements  
- Decrease administrative rework and operational costs  

---

## 🔗 Project Links

- 📊 [View Interactive Dashboard](https://public.tableau.com/views/Medicare_Denials_Dashboard/MedicareDenialsOverview?:language=en-US&:display_count=n&:origin=viz_share_link)  
- 🧠 [View SQL Queries](https://github.com/moonwalker2108/jilburtonDA/blob/main/jil-portfolio/project-1-medicare-denials/medicare_denials.sql)  




