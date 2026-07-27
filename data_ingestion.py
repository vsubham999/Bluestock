import os
import pandas as pd

data_path = "data/raw"

csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]

print(f"Total CSV files found: {len(csv_files)}")

for file in csv_files:
    file_path = os.path.join(data_path, file)

    print("\n"+"="*60)
    print(f"File Name : {file}")

    try:
        df = pd.read_csv(file_path)

        print(f"Shap : {df.shape}")

        print("\nData Types :")
        print(df.dtypes)

        print("\nFirst 5 rows :")
        print(df.head())

        print("\nMissing Values :")
        print(df.isnull().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")

print("\nData ingestion completed Successfully!")
