import pandas as pd

df = pd.read_csv("data.csv")
print("All Null Values:\n", df.isnull().sum())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df.head(6))
