import pandas as pd
from sqlalchemy import create_engine

# Extract: Read the CSV file
csv_file = 'employee_records.csv'
df = pd.read_csv(csv_file)

# Transform: Ensure 'salary' is numeric and 'age' is integer
# (Coerce errors to NaN, then drop rows with invalid data)
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df['age'] = pd.to_numeric(df['age'], errors='coerce', downcast='integer')
df = df.dropna(subset=['salary', 'age'])
df['salary'] = df['salary'].astype(float)
df['age'] = df['age'].astype(int)

# Add 'full_name' column
# Combine first_name and last_name, handling missing values gracefully
df['full_name'] = df['first_name'].fillna('') + ' ' + df['last_name'].fillna('')
df['full_name'] = df['full_name'].str.strip()

# Remove rows with missing or invalid emails (simple regex validation)
df = df[df['email'].str.contains(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', na=False)]

# Standardize 'department' to lowercase
df['department'] = df['department'].str.lower()

# Add 'salary_band' column
# Low: <50k, Medium: 50k–70k, High: >70k
def get_salary_band(salary):
    if salary < 50000:
        return 'Low'
    elif salary <= 70000:
        return 'Medium'
    else:
        return 'High'
df['salary_band'] = df['salary'].apply(get_salary_band)

# Extract 'hire_year' from 'hire_date'
df['hire_year'] = pd.to_datetime(df['hire_date'], errors='coerce').dt.year

# Load: Store the data into a SQLite database
db_file = 'employees.db'
engine = create_engine(f'sqlite:///{db_file}')
df.to_sql('employees', con=engine, if_exists='replace', index=False)

print('ETL process completed successfully!') 