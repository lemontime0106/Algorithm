word = list(input().rstrip())
result = list(input().rstrip())

flag = False

while result:
    if result[-1] == "A":
        result.pop()
    elif result[-1] == "B":
        result.pop()
        result.reverse()

    if word == result:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)