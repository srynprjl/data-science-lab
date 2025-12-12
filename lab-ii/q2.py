a = input("Enter a paragraph: ").strip().split(" ")

uw = set(a)
w = sorted(uw)
count = len(w)

print(f"Unique Words: {w}")
print(f"Count: {count}")
