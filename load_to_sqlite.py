import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("sqlite:///bluestock_mf.db")


clean_nav = pd.read_csv("data/processed/clean_nav.csv")
clean_transactions = pd.read_csv("data/processed/clean_transactions.csv")
clean_performance = pd.read_csv("data/processed/clean_performance.csv")
fund_master = pd.read_csv("data/raw/01_fund_master.csv")


fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
clean_nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
clean_transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
clean_performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("All datasets loaded successfully into bluestock_mf.db")