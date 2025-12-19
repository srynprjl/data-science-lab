# Writing and Reading JSON Data
import json

try:
    with open("q4.json") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File Not Found")
except json.JSONDecodeError:
    print("Cant decode json file")

print("ID | Name | Marks")
for i in data:
    print(f"{i['id']} | {i['name']} | {i['marks']}")
