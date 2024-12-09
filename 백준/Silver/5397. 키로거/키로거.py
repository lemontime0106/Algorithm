for _ in range(int(input())):
    password = input()
    left, right = [], []

    for i in password:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)

    left.extend(reversed(right))
    print(''.join(left))