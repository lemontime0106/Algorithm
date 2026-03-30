from collections import deque

n = int(input())
q = deque()
result = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        q.append(int(cmd[1]))

    elif cmd[0] == "pop":
        if q:
            result.append(str(q.popleft()))
        else:
            result.append("-1")

    elif cmd[0] == "size":
        result.append(str(len(q)))

    elif cmd[0] == "empty":
        result.append("0" if q else "1")

    elif cmd[0] == "front":
        if q:
            result.append(str(q[0]))
        else:
            result.append("-1")

    elif cmd[0] == "back":
        if q:
            result.append(str(q[-1]))
        else:
            result.append("-1")

print("\n".join(result))