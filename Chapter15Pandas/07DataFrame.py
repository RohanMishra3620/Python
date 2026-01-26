import pandas as pd

df_csv = pd.DataFrame({
    "Product": ["Soap", "Shampoo", "Toothpaste", "Oil"],
    "Price": [30, 120, 45, 150],
    "Unit_sold": [100, 60, 80, 50]
})

print(df_csv)
