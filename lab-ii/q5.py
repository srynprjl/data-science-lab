# Ask the user for a list of words. Reverse each word only if its length is even. Print the new list of words after processing.

words = input("Enter a list of words").replace(" ", ",").split(",")
pw = [ i[::-1] if len(i) % 2 == 0 else i for i in words  ]

# for i in words:
#     if len(i) % 2 == 0:
#         pw.append(i[::-1])
#     else:
#         pw.append(i)

print(pw)
