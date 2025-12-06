# Write a python program that prints the Fibonacci series up to n terms.

def fibonnaci(n):
    if(n <= 1):
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)

while True:
    try:
        a = int(input("Enter a number: "))
        if(a >= 0):
            break
    except :
        print("Please enter a integer")

for i in range(a):
    print(fibonnaci(i))


