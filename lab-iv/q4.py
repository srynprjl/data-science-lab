import random
random.seed(4090)
students = ["Shreyan", "Sandeep", "Yash", "Nayansha", "Anushka", "Pooja", "Ram", "Ram"]
try:
    volunteers = random.sample(list(set(students)), 3)
except ValueError:
    print("You are trying to take more volunteers than the total students")
print(volunteers)
