import pandas as pd
import sqlite3

# Read Excel file into a DataFrame
excel_file_path = 'Financial Analytics.xlsx'
df = pd.read_excel(excel_file_path)

# SQLite database file
sqlite_db_file = 'financial_data.db'

# Connect to SQLite database
conn = sqlite3.connect(sqlite_db_file)

# Save DataFrame to SQLite database
df.to_sql('financial_data', conn, index=False, if_exists='replace')

# Close the database connection
conn.close()

print(f"Data has been successfully imported from Excel and saved to {sqlite_db_file}.")
