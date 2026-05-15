# Consider the DataFrame QtrSales where each row contains the item
# category, item name and expenditure and group the rows by
# category, and print the average expenditure per category.

import pandas as pd

QtrSales = pd.DataFrame({
    "Category": ["Electronics", "Electronics", "Grocery", "Clothing", "Grocery"],
    "ItemName": ["Laptop", "Mobile", "Rice", "Shirt", "Oil"],
    "Expenditure": [50000, 20000, 3000, 2500, 1800]
})

print(QtrSales.groupby("Category")["Expenditure"].mean())