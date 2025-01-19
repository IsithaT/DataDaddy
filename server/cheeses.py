import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Number of records
n_records = 1000

# Generate dates
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(n_records)]

# Generate categorical data
departments = ["Sales", "Engineering", "Marketing", "HR", "Finance"]
locations = ["New York", "San Francisco", "Chicago", "Austin", "Seattle"]
experience_levels = ["Entry", "Mid", "Senior", "Lead"]
project_status = ["On Track", "Delayed", "Completed", "Not Started"]

# Generate numerical data with some correlations
base_salary = np.random.normal(75000, 15000, n_records)
years_experience = np.random.gamma(shape=2, scale=3, size=n_records) + 1
projects_completed = np.random.poisson(lam=5, size=n_records)
performance_score = 0.6 * (years_experience / 10) + 0.4 * np.random.normal(
    0.8, 0.1, n_records
)
performance_score = np.clip(performance_score, 0, 1)
training_hours = np.random.negative_binomial(n=5, p=0.5, size=n_records)
overtime_hours = np.random.exponential(scale=10, size=n_records)

# Create correlated satisfaction scores
job_satisfaction = 0.7 * performance_score + 0.3 * np.random.normal(
    0.75, 0.15, n_records
)
job_satisfaction = np.clip(job_satisfaction, 0, 1)

# Generate some missing values randomly
missing_mask = np.random.random(n_records) < 0.05

# Create the DataFrame
df = pd.DataFrame(
    {
        "date": dates,
        "department": np.random.choice(departments, n_records),
        "location": np.random.choice(locations, n_records),
        "experience_level": np.random.choice(experience_levels, n_records),
        "project_status": np.random.choice(project_status, n_records),
        "base_salary": base_salary,
        "years_experience": years_experience,
        "projects_completed": projects_completed,
        "performance_score": performance_score,
        "training_hours": training_hours,
        "overtime_hours": overtime_hours,
        "job_satisfaction": job_satisfaction,
    }
)

# Add some missing values
df.loc[missing_mask, ["training_hours", "overtime_hours", "job_satisfaction"]] = np.nan

# Add some derived features
df["salary_per_year_experience"] = df["base_salary"] / df["years_experience"]
df["is_high_performer"] = df["performance_score"] > 0.8
df["satisfaction_category"] = pd.qcut(
    df["job_satisfaction"].fillna(df["job_satisfaction"].mean()),
    q=3,
    labels=["Low", "Medium", "High"],
)

# Save to CSV
df.to_csv("employee_data.csv", index=False)

# Print summary statistics
print("\nDataset Summary:")
print(f"Total Records: {len(df)}")
print(f"\nNumerical Variables Summary:")
print(df.describe())
print(f"\nCategorical Variables Summary:")
print(df.select_dtypes(include=["object"]).describe())
print(f"\nMissing Values Summary:")
print(df.isnull().sum())
