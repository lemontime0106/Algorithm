from collections import deque

A, B = map(int, input().split())

q = deque()
q.append((A, 1))
cnt = 0

while q:
    number, cnt = q.popleft()
    if number > B:
        continue
    if number == B:
        print(cnt)
        break
    q.append((int(str(number) + "1"), cnt + 1))
    q.append((number * 2, cnt + 1))
else:
    print(-1)