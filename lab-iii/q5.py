def input_data():
    data = input("Enter a data: ")
    return data

def write_file(file):
    with open(file, "w") as f:
        data = input_data()
        f.write(data + "\n")

def read_file(file):
    try:
        with open(file, "r") as f:
            datas = f.readlines()
    except FileNotFoundError:
        print("File not Found")

    for i in datas:
        print(i.strip())

def append_file(file):
    try:
        with open(file, "a") as f:
            data = input_data()
            f.write(data + "\n")
    except FileNotFoundError:
        print("File not found")

def menu(file):
    while True:
        print("1. Write New Data")
        print("2. Read Data")
        print("3. Append New Data")
        print("4. Exit")
        try:
            option = int(input("1-4 "))
            if(option in range(1, 5)):
                match(option):
                    case 1:
                        write_file(file)
                        continue
                    case 2:
                        read_file(file)
                        continue
                    case 3:
                        append_file(file)
                        continue
                    case 4:
                        break;
            else:
                print("Enter values from 1-4")
        except ValueError:
            print("Enter a numeric value")
            continue

menu("q5.txt")
