# Series objects Temp1, temp2, temp3, temp 4 stores the temperature
# of days of week 1, week 2, week 3, week 4. Write a script to:-
# 1. Print average temperature per week
# 2. Print average temperature of entire month
import pandas as pd
week1 = pd.Series([23, 40, 20, 15])
week2 = pd.Series([25, 15, 12, 23])
week3 = pd.Series([21, 22, 19, 24])
week4 = pd.Series([29, 41, 12, 17])
print("Average Week1:", week1.mean())
print("Average Week2:", week2.mean())
print("Average Week3:", week3.mean())
print("Average Week4:", week4.mean())
df = pd.DataFrame([week1, week2, week3, week4],
                  index=["Week1", "Week2", "Week3", "Week4"])
print("Monthly Average Temperature:", df.values.mean())