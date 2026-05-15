# Write a program to create a DataFrame to store weight, age and
# name of three people. Print the DataFrame and its transpose.
import pandas as pd
df=pd.DataFrame({
        "Age":[21,19,18],
     "Name":["Rohan","Ravi","Raja"],
     "Weight":[75,67,89]
})
print("Orignal \n",df)
print("Transpose \n",df.T)