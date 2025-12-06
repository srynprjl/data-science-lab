# Write a program that prints all prime numbers up to a given number ‘n’

while True:
    try:
        a = int(input("Enter a number"))
        break
    except:
        print("Please enter a integer")


for i in range(2, a+1):
    prime = 0
    for j in range(2 , i+1):
        if(i % j == 0):
            prime += 1

    if(prime == 1):
        print(i)

