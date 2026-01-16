import pandas as pd

df = pd.read_csv("data.csv")

print(f"Duplicate Rows (After): \n {df.duplicated().sum()} \n")
df.drop_duplicates(inplace=True)
print(f"Duplicate Rows (Before): \n {df.duplicated().sum()} \n")
