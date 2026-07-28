-- 1. Top 5 Funds by AUM
SELECT
    d.fund_house,
    d.scheme_name,
    p.aum_crore
FROM dim_fund d
JOIN fact_performance p
ON d.amfi_code = p.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date)
ORDER BY month;

-- 3. SIP Inflow Year-over-Year Growth
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS sip_inflow
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY year
ORDER BY year;

-- 4. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1.0;

-- 6. Top 10 Funds by 1-Year Return
SELECT
    amfi_code,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 7. Average Expense Ratio by Category
SELECT
    d.category,
    AVG(p.expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
GROUP BY d.category;

-- 8. Number of Funds by Fund House
SELECT
    fund_house,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY fund_house
ORDER BY total_funds DESC;

-- 9. Average Sharpe Ratio
SELECT
    AVG(sharpe_ratio) AS average_sharpe_ratio
FROM fact_performance;

-- 10. Top 5 Funds by Latest NAV
SELECT
    amfi_code,
    nav
FROM fact_nav
ORDER BY nav DESC
LIMIT 5;