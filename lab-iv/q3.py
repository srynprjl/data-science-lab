def five():
    for i in range(1, 6):
        yield i

for n in five():
    print(n)



