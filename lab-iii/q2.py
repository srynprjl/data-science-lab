# import re

try:
    sum = 0
    length = 0
    with open("q2.txt", "r") as f:
        for i in f.readlines():
            # match = re.search(r"\d+", i)
            # if not match:
            #     continue
            # i = match.group()
            try:
                sum += float(i) if "." in i else int(i)
                length += 1
            except ValueError:
                continue
except FileNotFoundError:
    print("File not found." )

print(f"Sum : {sum}")
print(f"Average: {sum/length}")
