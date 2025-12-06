## Define a function that takes two numbers as arguments, and returns their greatest common divisor (GCD).

def gcd(a, b):
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        break
    except:
        print("Invalid Input. Enter number only.")

print(gcd(a, b))
