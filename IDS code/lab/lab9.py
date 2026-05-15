# Write a program to show functions on a subset of Dataframe.
import pandas as pd
df = pd.DataFrame({
    "Name": ["Rohan","Shubham","Ram","Ravi"],
    "Age": [21,20,30,23],
    "Marks": [97,79,100,25]
})
subset = df[['Age', 'Marks']]
print("Functions on Subset:") 
print(subset.agg(['mean', 'min', 'max',"sum","std"]).round(2))
