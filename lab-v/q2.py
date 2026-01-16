import pandas as pd

df = pd.read_csv("data.csv")
print("Columns:", df.columns)
print("\nDatatype:\n", df.dtypes)
print("\nStats:\n", df.describe())
