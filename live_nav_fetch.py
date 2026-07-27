import requests
import pandas as pd
import os

scheme_code = "119551"  # Kotak Bluechip - Direct Plan - Growth

url = f"https://api.mfapi.in/mf/{scheme_code}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data['data'])

    os.makedirs("data/raw", exist_ok=True)

    output_file = "data/raw/live_nav_data.csv"
    df.to_csv(output_file, index=False)

    print(f"NAV data Saved Successfully to {output_file}")
else:
    print("Failed to fetch NAV data.")