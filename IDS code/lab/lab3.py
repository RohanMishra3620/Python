# Perform sorting on Series data.
import pandas as pd

data = pd.Series([10,100,30,90,20,40])
print("Sorting by index in ASCENDING order :")
print(data.sort_index())
print("Sorting by index in DESCENDING order:")
print(data.sort_index(ascending=False))
print("Sorting by VALUES in ASCENDING order:")
print(data.sort_values())
print("Sorting by VALUES in DESCENDING order:")
print(data.sort_values(ascending=False))