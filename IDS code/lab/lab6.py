# Program to use cumprod(),cumsum(), cummin() and cummax().
import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Name": ["Rohan","Shubham","Ram","Ravi"],
    "Age": [21,20,30,23],
    "Marks": [97,79,100,np.nan]
})

print("CUMMAX:\n", data.cummax())
print("CUMMIN:\n", data[["Age","Marks"]].cummin(skipna=True))
print("CUMPROD:\n", data["Marks"].cumprod())
print("CUMSUM:\n", data["Age"].cumsum())