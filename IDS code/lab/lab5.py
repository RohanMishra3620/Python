# Program to shoe Deleting/Renaming Columns/Rows
import pandas as pd
data=pd.DataFrame({"Name":["Rohan","Shubham","Ram","Ravi","Raju"],
                   "age":[21,20,30,23,29],
                   "Marks":[90,89,65,78,45]
                   })
print("Orignal : ")
print(data,"\n")
print("After update : ")
data=data.rename(columns={"age":"Age"})
data=data.rename(index={0:"A",1:"B",2:"C",3:"D",4:"E"})
data=data.drop(columns="Marks")
data=data.drop(index="E")
print(data)