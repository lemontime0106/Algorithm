from collections import deque

N = int(input())
q = deque([i for i in range(1, N+1)])

while True:
    if len(q) == 1:
        print(q[0])
        break

    q.popleft()
    q.append(q.popleft())
