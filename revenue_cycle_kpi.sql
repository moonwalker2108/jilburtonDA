/* Revenue-Cycle KPIs – hospital billing snapshot */
SELECT
    snapshot_date,
    SUM(dnfb_amount)          AS dnfb,
    AVG(discharge_to_bill_hours) AS avg_lag,
    SUM(aged_ar_120plus)      AS aged_ar
FROM rc_kpi_daily
WHERE snapshot_date >= CURRENT_DATE - 90
GROUP BY snapshot_date
ORDER BY snapshot_date DESC;