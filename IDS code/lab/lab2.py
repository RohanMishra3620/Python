# Create a Series and print all the elements that are above 75th percentile.
import pandas as pd
data=pd.Series(data=[10,15,90,100,30],index=["Rohan","Ravi","Raju","Ram","Rohit"])
data.index.name="Name"
data.name="Marks"
per=data.quantile(0.75)
print(data[data>=per])
