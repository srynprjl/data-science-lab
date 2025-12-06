def c_to_k(c):
    return c + 273.15
def c_to_f(c):
    return (c* 9/5)+32

while True:
    try:
        t = float(input("Enter the temperature in celcius: "))
        break
    except:
        print("Invalid input")

choice = None
while choice not in ("F", "K"):
    choice = input("Enter F for fahrenheit, and K for kelvin").upper()
    if(choice not in ("F", "K")):
        print("Invalid input.")


if choice == "F":
    temp = c_to_f(t)
    if(temp.is_integer()):
        temp = int(temp)
    print(f"Temp: {temp} F")
else:
    temp = c_to_k(t)
    if(temp.is_integer()):
        temp = int(temp)
    print(f"Temp: {temp} K")
