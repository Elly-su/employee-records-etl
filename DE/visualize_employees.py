import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Connect to the database and load the data
db_file = '../employees.db'  # if running from DE
engine = create_engine(f'sqlite:///{db_file}')
df = pd.read_sql('SELECT * FROM employees', engine)

# Set seaborn style
sns.set(style='whitegrid')

# to  Print salary summary statistics
print('Salary Summary Statistics:')
print(df['salary'].describe())
print('\nSample Salaries:')
print(df['salary'].head(10))

# 1. Salary Distribution (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(df['salary'], bins=20, kde=True, color='skyblue')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.show()

# 2. Number of Hires per Year
plt.figure(figsize=(8, 5))
hire_counts = df['hire_year'].value_counts().sort_index()
sns.barplot(x=hire_counts.index, y=hire_counts.values, palette='viridis')
plt.title('Number of Hires per Year')
plt.xlabel('Year')
plt.ylabel('Number of Hires')
plt.tight_layout()
plt.show() 
