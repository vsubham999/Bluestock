# Data Dictionary

## 1. dim_fund

| Column Name | Data Type | Description | Source |
|-------------|-----------|-------------|--------|
| amfi_code | TEXT | Unique AMFI Scheme Code | fund_master.csv |
| fund_house | TEXT | Mutual Fund House Name | fund_master.csv |
| scheme_name | TEXT | Scheme Name | fund_master.csv |
| category | TEXT | Fund Category | fund_master.csv |
| sub_category | TEXT | Fund Sub Category | fund_master.csv |
| risk_category | TEXT | Risk Category | fund_master.csv |

---

## 2. fact_nav

| Column Name | Data Type | Description | Source |
|-------------|-----------|-------------|--------|
| amfi_code | TEXT | AMFI Scheme Code | nav_history.csv |
| date | DATE | Date | nav_history.csv |
| nav | REAL | Net Asset Value | nav_history.csv |
| daily_return | REAL | Daily NAV Return | Calculated |

---

## 3. fact_transactions

| Column Name | Data Type | Description | Source |
|-------------|-----------|-------------|--------|
| transaction_id | INTEGER | Transaction ID | investor_transactions.csv |
| amfi_code | TEXT | AMFI Scheme Code | investor_transactions.csv |
| investor_id | TEXT | Investor ID | investor_transactions.csv |
| transaction_date | DATE | Transaction Date | investor_transactions.csv |
| transaction_type | TEXT | SIP/Lumpsum/Redemption | investor_transactions.csv |
| amount_inr | REAL | Transaction Amount | investor_transactions.csv |
| units | REAL | Units Purchased/Redeemed | investor_transactions.csv |
| kyc_status | TEXT | KYC Verification Status | investor_transactions.csv |

---

## 4. fact_performance

| Column Name | Data Type | Description | Source |
|-------------|-----------|-------------|--------|
| amfi_code | TEXT | AMFI Scheme Code | scheme_performance.csv |
| return_1yr_pct | REAL | One Year Return (%) | scheme_performance.csv |
| return_3yr_pct | REAL | Three Year Return (%) | scheme_performance.csv |
| return_5yr_pct | REAL | Five Year Return (%) | scheme_performance.csv |
| sharpe_ratio | REAL | Sharpe Ratio | scheme_performance.csv |
| expense_ratio_pct | REAL | Expense Ratio (%) | scheme_performance.csv |
| aum_crore | REAL | Assets Under Management (₹ Crore) | scheme_performance.csv |

---

## Data Sources

- fund_master.csv
- nav_history.csv
- investor_transactions.csv
- scheme_performance.csv
- benchmark_indices.csv
- live_nav_data.csv

