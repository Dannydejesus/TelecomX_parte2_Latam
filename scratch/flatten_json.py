import json
import pandas as pd

with open('data/raw/TelecomX_Data.json', 'r') as f:
    data = [json.loads(line) for line in f]

# Flatten the data
df = pd.json_normalize(data)
print("Flattened columns:", df.columns.tolist())

# Save to CSV
df.to_csv('data/raw/TelecomX_Data_flat.csv', index=False)
print("Saved flattened CSV to data/raw/TelecomX_Data_flat.csv")
