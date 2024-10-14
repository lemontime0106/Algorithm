from collections import deque

word = deque(input().strip())
N = int(input())
lst = [input().split() for _ in range(N)]

left = word
right = deque()

for order in lst:
    if order[0] == "P":
        left.append(order[1])

    elif order[0] == "L":
        if left:
            right.appendleft(left.pop())

    elif order[0] == "D":
        if right:
            left.append(right.popleft())

    elif order[0] == "B":
        if left:
            left.pop()

print("".join(left) + "".join(right))