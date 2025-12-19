import csv
try:
    with open("q3.csv", "r", newline="") as f:
        lines = csv.reader(f)
        next(lines)
        print("Roll | Name | Marks")
        for rows in lines:
            try:
                roll = int(rows[0])
                name = rows[1]
                marks = float(rows[2]) if "." in rows[2] else int(rows[2])
                print(f"{roll} | {name} | {marks}")
            except ValueError:
                print("Data conversion error!!")

except FileNotFoundError:
    print("File not found!!!")
