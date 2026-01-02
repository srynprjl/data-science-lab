#Write a program that takes a list of numbers as input, and returns the largest number in the list.

def largest(nums: list):
    if not nums:
        return None

    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest

list = []
try:
    a = input("Enter a number or leave blank to stop")
    a = a.split()
    # print(a)
    list = [float(i.strip()) if "." in i else int(i.strip()) for i in a]
except:
    print("Invalid input. Only input float or list numbers")

print(f"Largest Num: ", largest(list))
