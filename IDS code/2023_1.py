import pandas as pd
df=pd.DataFrame({"Week":["Mon","Tues","Wed","Thr","Fri","Sat","Sun"],
                  "Rainfall":[10,20,15,20,15,20,15]
                  })
print(df)
print("Mean:", df["Rainfall"].mean())
print("Max:", df["Rainfall"].max())
print("Min:", df["Rainfall"].min())
print("Q1:", df["Rainfall"].quantile(0.25))
print("Median:", df["Rainfall"].quantile(0.50))
print("Q3:", df["Rainfall"].quantile(0.75))
print("Std Dev:", df["Rainfall"].std())