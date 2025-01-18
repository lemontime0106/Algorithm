for _ in range(int(input())):
    op = input()

    if "+" in op:
        a, b = map(int, op.split("+"))
        print(a + b)
    else:
        print("skipped")