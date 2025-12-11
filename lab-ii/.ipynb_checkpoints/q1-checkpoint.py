'''
Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...]. Compute
the average rating, find the highest-rated movie, and list all movies with rating above the
average
'''


a = input("Movie Name-Rating, Movie2-Rating: ").replace(" ", "").strip()
a = a.split(",")
a = [item for item in a if "-" in item]
a = [ tuple(item.split("-")) for item in a]

print(a)
