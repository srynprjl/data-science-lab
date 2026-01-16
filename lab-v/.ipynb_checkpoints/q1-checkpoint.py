import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [20, 21, 19, 22, 20, 21],
    "Marks": [85, 55, 92, 40, 78, 95],
}

df = pd.DataFrame(data)

print("Rows:\n", df.head())
print("\nShape:", df.shape)
