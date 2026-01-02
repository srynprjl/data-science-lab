'''Write a Python script that takes a list of student marks and sorts them in descending order (highest to lowest) using either the sorted() function or the .sort() method.'''

marks = [85, 92, 78, 60, 95, 88]
# sorted_marks = sorted(reverse=True)
marks.sort(reverse=True)
print(marks)
