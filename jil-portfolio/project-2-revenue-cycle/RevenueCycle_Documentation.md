# Revenue-Cycle KPI Report  
**Tools:** SQL + Excel (Power Query)  
**Frequency:** Daily refresh (Power Query → SQL Server)  

### KPIs Tracked
- DNFB (Discharged Not Final Billed)  
- Discharge-to-Bill Lag (hours)  
- A/R &gt; 120 Days (%)  

### How to Reproduce
1. Open Excel → Data → Get Data → From SQL Server  
2. Paste `revenue_cycle_kpi.sql` → load to data model  
3. Insert pivot charts → save as `RevenueCycle_KPI.xlsx`