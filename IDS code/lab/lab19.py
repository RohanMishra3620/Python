# Create a DataFrame having age, name, weight of five students.
# Write a program to display only the weight of first and fourth rows.
import pandas as pd
df=pd.DataFrame({
                   "Age":[21,19,18,20,21],
                   "Name":["Rohan","Ravi","Raja","Ram","Rohit"],
                   "Weight":[75,67,89,65,96]
})
print("Weight of first and fourth rows \n",df.iloc[[0,3]]["Weight"])