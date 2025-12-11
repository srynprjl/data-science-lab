a = input("Enter a paragraph: ").split(" ")


uw = set(a)
w = list(uw)
w = sorted(w)
count = len(w)

print(f"Unique Words: {w}")
print(f"Count: {count}")
