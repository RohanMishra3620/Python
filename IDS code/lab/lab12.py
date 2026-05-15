# Create a DataFrame based on E-Commerce data and generate mean, mode, median.
import pandas as pd
data = pd.DataFrame({
    "CustomerName": ["Rohan", "Ravi", "Raja", "Rohit", "Ram"],
    "Product": ["Laptop", "Mobile", "Laptop", "Laptop", "Watch"],
    "Price": [150000, 25000, 250000, 100000, 3000],
    "Quantity": [1, 2, 3, 1, 2],
}, index=[101, 102, 103, 104, 105])

print(data)
print("\nMean of Quantity:", data["Quantity"].mean())
print("Median of Price:", data["Price"].median())
print("Mode of Product:", data["Product"].mode())