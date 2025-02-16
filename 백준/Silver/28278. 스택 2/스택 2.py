import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    case = list(map(int, sys.stdin.readline().split()))

    if case[0] == 1:
        stack.append(case[1])
    elif case[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif case[0] == 3:
        print(len(stack))
    elif case[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif case[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)