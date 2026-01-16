import pandas as pd

data = {
    "Name": ["Aabhash", "Sandeep", "Shreyan", "Amit", "Yash", "Anushka"],
    "Age": [20, 21, 19, 22, 20, 21],
    "Marks": [85, 55, 92, 40, 78, 95],
}

df = pd.DataFrame(data)
# df.to_csv("data.csv", index=False)
print("Data:\n", df.head())
print("\nShape:", df.shape)
