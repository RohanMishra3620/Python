# Write a program to find mean absolute deviation on a DataFrame.
import pandas as pd
df = pd.DataFrame({
    "Name": ["Rohan","Shubham","Ram","Ravi"],
    "Age": [21,20,30,23],
    "Marks": [97,79,100,25]
})
mad = (df['Age'] - df['Age'].mean()).abs().mean()
print("Mean absolute deviation",mad)
