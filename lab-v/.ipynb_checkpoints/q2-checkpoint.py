import pandas as pd

df = pd.read_csv("your_file.csv")

print("Column Names:", df.columns)
print("\nData Types:\n", df.dtypes)
print("\nBasic Statistics:\n", df.describe())
