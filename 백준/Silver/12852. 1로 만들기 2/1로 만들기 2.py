from collections import deque

N = int(input())
q = deque()
q.append([N])
answer = []

while q:
    a = q.popleft()
    x = a[0]

    if x == 1:
        answer = a
        break

    if x % 3 == 0:
        q.append([x // 3] + a)

    if x % 2 == 0:
        q.append([x // 2] + a)

    q.append([x-1] + a)

print(len(answer) - 1)
print(*answer[::-1])