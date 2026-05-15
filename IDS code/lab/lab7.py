# Write a program to implement pivot() and pivot-table() on a DataFrame.
import pandas as pd
data = pd.DataFrame({
    "Name": ["Rohan","Rohan","Shubham","Shubham"],
    "Subject": ["Maths","SST","SST","Maths"],
    "Marks": [97,79,100,80]
})
print("\nOriginal Data:\n", data)
print("\nPivot:\n",data.pivot(index="Name", columns="Subject", values="Marks"))

data = pd.DataFrame({
    "Name": ["Rohan","Rohan","Rohan","Shubham","Shubham"],
    "Subject": ["Maths","SST","Maths","SST","Maths"],
    "Marks": [97,79,90,100,80]
})
print("\nOriginal Data:\n", data)
print("\nPivot Table :\n",data.pivot_table(index="Name", columns="Subject", values="Marks", aggfunc="mean"))
