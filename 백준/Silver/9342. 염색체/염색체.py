import re
for _ in range(int(input())):
    word = input()
    check = re.compile("^[A-F]?A+F+C+[A-F]?$")
    if check.match(word) == None:
        print("Good")
    else:
        print("Infected!")