import json
import pandas as pd
import numpy as np

with open('data/raw/TelecomX_Data.json', 'r') as f:
    data = json.load(f)

# Flatten the data
df = pd.json_normalize(data)

# Rename columns to be more standard (remove dots)
df.columns = [c.replace('.', '_') for c in df.columns]

# Convert TotalCharges to numeric (it might have empty strings for new customers)
if 'account_Charges_Total' in df.columns:
    df['account_Charges_Total'] = pd.to_numeric(df['account_Charges_Total'], errors='coerce')

print("Flattened columns:", df.columns.tolist())
print("Total rows:", len(df))

# Save to CSV
csv_path = 'data/raw/TelecomX_Data_flat.csv'
df.to_csv(csv_path, index=False)
print(f"Saved flattened CSV to {csv_path}")
