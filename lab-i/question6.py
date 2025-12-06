# Write a program that checks if a given number is even or odd.

def isEvenOrOdd(number):
    if( number % 2 == 0 ):
        return "even"
    else:
        return "odd"

while True:
    try:
        a = int(input("Enter a number: "))
        break
    except:
        print("Enter an integer.")

print(f"{a} is an {isEvenOrOdd(a)} number")
