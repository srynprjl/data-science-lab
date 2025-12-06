# Write a program that checks if a given string is palindrome.

a = input("Enter a string: ")
b = a[::-1]

if(a == b):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

