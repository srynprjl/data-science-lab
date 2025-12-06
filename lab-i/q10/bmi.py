def bmi():
    try:
        while True:
            h = input("Enter f for [feet/inches] or c for [centimeters]").lower()
            if(h == "f"):
                foot = float(input("Enter feet"))
                inch = float(input("Enter the inches"))
                height = (foot * 12 + inch) * 0.0254
                break
            elif(h == "c"):
                height = float(input("Enter your height in cm"))
                height = height / 100
                break
            else:
                print("Invalid input! Please only write f or c. ")

        while True:
            w = input("Enter p for pounds and k for kg").lower()
            if(w == "p"):
                p = float(input("Enter weight in pounds"))
                weight = p * (0.4535)
                break
            elif(w == "k"):
                weight = float(input("Enter weight in kilogram. "))
                break
            else:
                print("Invalid Input! Please only write k or c")

        bmi = weight/(height*height)
        bmi_category(bmi)
        return bmi
    except:
        print("Invalid Input")



def bmi_category(bmi):
    if(bmi < 18.5):
        print("Underweight")
    elif(bmi >= 18.5 and bmi <=24.9):
        print("Normal Weight")
    elif(bmi >= 25 and bmi <=29.9):
        print("Normal Weight")
    elif(bmi >= 30 ):
        print("Obese")
    else:
        print("Invalid Input. ")
