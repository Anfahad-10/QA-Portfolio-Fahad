import pandas as pd

# Created Dummy Data with purposeful errors in it

data = {
    'User_ID': [101, 102, 103, 104, 105],
    'Name': ['Fahad', 'Rahul', 'Amit', 'Sara', 'Priya'],
    'Email': ['fahad@test.com', 'rahul@test', 'amit@test.com', 'sara_test.com', 'priya@test.com'],
    'Age': [25, 17, 30, -5, 22]
}

# Save it as a CSV file

df = pd.DataFrame(data)
df.to_csv('user_data.csv', index=False)

print("Setup Complete: 'user_data.csv' has been created with errors!")

import pandas as pd
import re 

# 1. Load the Data
df = pd.read_csv('user_data.csv')
print("--- STARTING AUTOMATED VALIDATION ---")

# 2. Define the Rules (The "Test Plan")
error_log = []

for index, row in df.iterrows():
    user = row['Name']
    email = row['Email']
    age = row['Age']

    # RULE 1: Age must be positive and over 18
    if age < 0:
        error_log.append(f"Row {index+1}: User '{user}' has Impossible Age ({age})")
    elif age < 18:
        error_log.append(f"Row {index+1}: User '{user}' is Underage ({age})")

    # RULE 2: Email must contain '@' and '.'
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        error_log.append(f"Row {index+1}: User '{user}' has Invalid Email format ({email})")

# 3. Generate the Bug Report
print(f"\nScanning {len(df)} records...")
print(f"Found {len(error_log)} Data Defects:\n")

for error in error_log:
    print(f"[FAIL] {error}")

if len(error_log) == 0:
    print("\n[PASS] No Data Defects Found.")