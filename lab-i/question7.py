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
# flag = False
while True:
    try:
        a = input("Enter a number or leave blank to stop")
        if not a:
            break
        if("." in a):
            list.append(float(a))
        else:
            list.append(int(a))

    except:
        print("Invalid input. Only input float or list numbers")



print(largest(list))
