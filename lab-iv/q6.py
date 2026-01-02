from functools import reduce
names = ["Shreyan", "Sandeep", "Yash"]
scores = [85, 90, 75]
students = zip(names, scores)
total = reduce(lambda acc, data: acc + data[1], students, 0)
print(total)
