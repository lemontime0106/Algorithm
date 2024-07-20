from collections import deque

N, M = map(int, input().split())
number = list(map(int, input().split()))

lst = deque([i for i in range(1, N + 1)])

cnt = 0
for n in number:
    while True:
        if lst[0] == n:
            lst.popleft()
            break
        else:
            if lst.index(n) <= len(lst) // 2:
                lst.rotate(-1)
                cnt += 1
            else:
                lst.rotate(1)
                cnt += 1
print(cnt)