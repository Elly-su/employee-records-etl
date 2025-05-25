import pandas as pd
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine('sqlite:///employees.db')

# Example: Show the first 5 employees
query = "SELECT * FROM employees LIMIT 5"
df = pd.read_sql(query, engine)
print(df)

# Example: Count employees by department
query2 = "SELECT department, COUNT(*) as num_employees FROM employees GROUP BY department"
df2 = pd.read_sql(query2, engine)
print(df2)