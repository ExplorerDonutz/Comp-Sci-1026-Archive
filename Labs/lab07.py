values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for cur in values:
    print("The value is :", values[cur])
    if type(values[cur]) == str:
        raise ValueError("This is a string!")

# ---- Part 2 ----

filename = input("Enter filename: ")

# First exception is IOError
try:
    infile = open(filename, "r")
    line = infile.readline()
except IOError as f:
    print("This file does not exist!")

try:
    value = int(line)
except ValueError as error:
    print("Value Error: ", error)
