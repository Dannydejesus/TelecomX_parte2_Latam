import duckdb
import pandas as pd

con = duckdb.connect()
json_path = 'data/raw/TelecomX_Data.json'

print("--- SCHEMA ---")
describe = con.execute(f"DESCRIBE FROM read_json_auto('{json_path}')").df()
print(describe)

print("\n--- ROW COUNT ---")
count = con.execute(f"SELECT count(*) FROM read_json_auto('{json_path}')").fetchone()[0]
print(f"Total rows: {count}")

print("\n--- SAMPLE DATA ---")
sample = con.execute(f"SELECT * FROM read_json_auto('{json_path}') LIMIT 5").df()
print(sample)

# Convert to CSV for data-analysis skill
csv_path = 'data/raw/TelecomX_Data.csv'
con.execute(f"COPY (SELECT * FROM read_json_auto('{json_path}')) TO '{csv_path}' (FORMAT CSV, HEADER)")
print(f"\nSaved CSV to {csv_path}")
