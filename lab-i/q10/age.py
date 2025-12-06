import datetime
def calculate_birth_year(age):
    year = datetime.datetime.now().year
    birth = year - age
    if((birth % 4 == 0 and birth % 100 != 0) or birth % 400 == 0):
        print(f"Your birthyear {birth}  is a leap year")
    else:
        print(f"Your birthyear {birth} is a not a leap year")
    return birth

def birth_year():
    try:
        age = int(input("Enter your age: "))
    except:
        print("Invalid age!")
    return age

