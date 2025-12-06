from age import birth_year, calculate_birth_year
from bmi import bmi

def army_check(age, bmi):
    if( (age >= 18 and age <= 40) and ( bmi >= 18.5 and bmi <= 29.9) ):
        print("You are eligible for army entrance. ")
    else:
        print("You are not eligible for army entrance")

try:
    age = birth_year()
    birthyear = calculate_birth_year(age)
    bmi = bmi()

    print(f"Age {age}")
    print(f"BMI: {bmi}")

    army_check(age, bmi)
except:
    pass
