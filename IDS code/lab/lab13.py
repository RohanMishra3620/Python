# Create a DataFrame based on employee data and generate quartile and variance.
import pandas as pd
data = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105],
    "Name": ["Rohan", "Amit", "Rohan", "Sneha", "Amit"],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
    "Salary": [30000, 40000, 35000, 32000, 42000]
})
print("Q1 (25%):", data["Salary"].quantile(0.25))
print("Q2 (Median):", data["Salary"].quantile(0.5))
print("Q3 (75%):", data["Salary"].quantile(0.75))
print("\nVariance of Salary:", data["Salary"].var())