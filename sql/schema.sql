-- Create Dimension Table
CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

-- Create NAV Fact Table
CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    nav_date DATE,
    nav REAL,
    daily_return REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Create Transactions Fact Table
CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    amfi_code TEXT,
    investor_id TEXT,
    transaction_date DATE,
    transaction_type TEXT,
    amount REAL,
    units REAL,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Create Performance Fact Table
CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    sharpe_ratio REAL,
    expense_ratio REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Create Benchmark Table 
CREATE TABLE dim_benchmark (
    benchmark_id INTEGER PRIMARY KEY AUTOINCREMENT,
    benchmark_name TEXT,
    benchmark_value REAL,
    benchmark_date DATE
);