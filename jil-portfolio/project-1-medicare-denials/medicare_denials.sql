/* Medicare Claims Denials – last 12 months */
SELECT
    DATE_TRUNC('month', claim_date)  AS month,
    denial_reason_code,
    COUNT(*)                           AS denied_claims,
    SUM(charge_amount)                 AS denied_revenue
FROM medicare_claims
WHERE claim_status = 'DENIED'
  AND claim_date >= CURRENT_DATE - INTERVAL '12 months'
GROUP BY 1,2
ORDER BY 1 DESC;