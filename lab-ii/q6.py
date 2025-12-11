'''
Represent a small map as a dictionary like {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}. Ask the user to input a path, e.g., ["A", "C", "D"]. Check if each consecutive step is connected and print "Valid path" or "Invalid path"
'''

def validate_path(inp: list, map: dict):
    if(not inp):
        return "Valid path"

    length = len(inp)
    if(length == 1 and inp[0] in map.keys()):
        return "Valid path"

    for i in range(length - 1):
        now = inp[i]
        next = inp[i+1]
        val = next in map[now]
        if(val):
            path = "Valid path"
        else:
            path = "Invalid path"
            break
    return path

map =  {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}
val = ["B", "C", "C" ]

values = input("Enter the path: ").split("-")


print(validate_path(values, map))
