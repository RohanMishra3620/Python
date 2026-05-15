# 1. Create a pandas series from a dictionary of values and an ndarray.
import pandas as pd
import numpy as np
data = {"Rohan": 21,"Shubham": 20,"Ram": 30,"Ravi": 23,"Raju": 29}
dict = pd.Series(data)
print(dict)
print()
ages = np.array([21,20,30,23,29])
arr = pd.Series(ages, index=["Rohan","Shubham","Ram","Ravi","Raju"])
print(arr)









