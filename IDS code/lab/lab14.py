# Program to implement Skewness on Random data.

import pandas as pd
data = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105],
    "Name": ["Rohan", "Amit", "Rohan", "Sneha", "Amit"],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
    "Salary": [30000, 40000, 35000, 32000, 42000]
})
print(data["Salary"].skew())


# 0:Symmetrical data             
# +ve:Right skewed (tail on right) 
# -ve:Left skewed (tail on left)   
