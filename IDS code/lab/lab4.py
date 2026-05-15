# Perform sorting on DataFrames data.
import pandas as pd

data=pd.DataFrame({"Name":["Rohan","Shubham","Ram","Ravi","Raju"],
                   "Age":[21,20,30,23,29]})

print("Sorting by index in ASCENDING order :")
print(data.sort_index())
print("Sorting by index in DESCENDING order:")
print(data.sort_index(ascending=False))
print("Sorting by VALUES in ASCENDING order:")
print(data.sort_values(by="Name"))
print("Sorting by VALUES in DESCENDING order:")
print(data.sort_values(by="Name",ascending=False))
print("Sorting by VALUES in ASCENDING order:")
print(data.sort_values(by="Age"))
print("Sorting by VALUES in DESCENDING order:")
print(data.sort_values(by="Age",ascending=False))