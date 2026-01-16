import pandas as pd

df = pd.read_csv("data.csv")

high_marks = df[df["Marks"] > 60]
subset = df[["Name", "Marks"]]

print(f"High Marks:\n {high_marks} \n")
print(f"Subset:\n {subset} \n")

