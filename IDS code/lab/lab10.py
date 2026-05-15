# Adding/Modifying a row in DataFrame.
import pandas as pd
df = pd.DataFrame({
    "Name": ["Rohan","Shubham","Ram","Ravi"],
    "Age": [21,20,30,23],
    "Marks": [97,79,100,25]
})
print(df,"\n")
new=pd.DataFrame({
     "Name": ["Raja","Rohit"],
    "Age": [30,23],
 "Marks": [95,75]
})
df=pd.concat([df,new],ignore_index=True)
df.iloc[2,0]="Raj"
print(df)