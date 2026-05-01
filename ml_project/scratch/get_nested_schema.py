import duckdb
con = duckdb.connect()
json_path = 'data/raw/TelecomX_Data.json'

# Get all column names and types, including nested fields
res = con.execute(f"DESCRIBE FROM read_json_auto('{json_path}')").df()
print(res)

# Let's see the keys in the structs
for col in ['customer', 'phone', 'internet', 'account']:
    keys = con.execute(f"SELECT map_keys(CAST({col} AS MAP(VARCHAR, JSON))) FROM read_json_auto('{json_path}') LIMIT 1").fetchone()[0]
    print(f"{col} keys: {keys}")
