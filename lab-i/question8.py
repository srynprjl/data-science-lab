# Write a program that checks if a year is a leap year.

def is_leap(year):
    if(year % 400 == 0):
        return True
    elif(year % 100 == 0):
        return False
    elif(year % 4 == 0):
        return True
    else:
        return False

try:
    while True:
        y = int(input("Enter a year"))
        if (y < 0):
            print("Enter a positive year")
            continue
        break
except:
    print("Invalid Input. Year should be an whole number (integer)")

leap = is_leap(y)
if leap:
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")
