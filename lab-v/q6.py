import pandas as pd

df = pd.read_csv("data.csv")
q1 = df["Marks"].percentile(25)
q3 = df["Marks"].percentile(75)
iqr = q3 - q1

low = q1 - 1.5 * iqr
up = q3 + 1.5 * iqr
new_data = df[(df["Marks"] >= low) & (df["Marks"] <= up)]
