'''
Store student names as keys and marks (list of integers) as values in a dictionary. Compute
each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks.
'''

students = {
    "Shreyan": [90,90,90,90,90],
    "Yash": [79,65,94,87,67],
    "Sandeep": [1, 2, 11, 0, 3]
}

def take_user_input():
    # a-[1,2,3,4,5,6,7,8,9],
    std = {}
    a = input("Enter student name and marks: ").split(" ")
    for items in a:
        word = items.split("-")
        print(word)
        name = word[0]
        marks = word[1].removeprefix("[").removesuffix("]").split(",")
        marks = [int(items) for items in marks]
        std[name] = marks

    return std



def calculate_grade(marks: int):
    if(marks > 100 or marks < 0):
        return None
    elif(marks >= 90):
        return 'A'
    elif(marks >= 80):
        return 'B'
    elif(marks >= 70):
        return 'C'
    elif(marks >= 60):
        return 'D'
    elif(marks >= 50):
        return 'E'
    else:
        return 'F'

def calculate_average(students: dict):
    std={}
    for name, marks in students.items():
        total = 0
        for i in marks:
            total += i
        avg = total / len(marks)
        grade = calculate_grade(avg)
        std[name]= {"Average": avg, "Grade": grade}
    return std

def sort(item):
    return item[1]['Average']

def top_two_students(std: dict):
    results = sorted(std.items(), key=sort, reverse=True)
    return results[:2]

students = take_user_input()

std = calculate_average(students)
print(top_two_students(std))
