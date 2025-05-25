import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Determine script location and set paths accordingly
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..'))

# Path to database and visualizations folder
if os.path.exists(os.path.join(project_root, 'employees.db')):
    db_file = os.path.join(project_root, 'employees.db')
else:
    db_file = os.path.join(script_dir, 'employees.db')

viz_dir = os.path.join(project_root, 'visualizations')
os.makedirs(viz_dir, exist_ok=True)

# Connect to the database and load the data
engine = create_engine(f'sqlite:///{db_file}')
df = pd.read_sql('SELECT * FROM employees', engine)

sns.set(style='whitegrid')

# 1. Salary Distribution (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(df['salary'], bins=20, kde=True, color='skyblue')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.savefig(os.path.join(viz_dir, 'salary_distribution.png'))
plt.close()

# 2. Number of Hires per Year
plt.figure(figsize=(8, 5))
hire_counts = df['hire_year'].value_counts().sort_index()
sns.barplot(x=hire_counts.index, y=hire_counts.values, palette='viridis')
plt.title('Number of Hires per Year')
plt.xlabel('Year')
plt.ylabel('Number of Hires')
plt.tight_layout()
plt.savefig(os.path.join(viz_dir, 'hires_per_year.png'))
plt.close()

print(f'Visualizations saved in the {viz_dir} folder.') 