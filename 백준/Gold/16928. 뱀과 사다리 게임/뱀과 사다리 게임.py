from collections import deque

N, M = map(int, input().split())

MAP = [0] * 101
visited = [False] * 101

ladder = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b

snake = {}
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b

q = deque()
q.append(1)
visited[1] = True

while q:
    v = q.popleft()

    for i in range(1, 7):
        cur = v + i

        if 0 < cur <= 100 and not visited[cur]:
            if cur in ladder:
                cur = ladder[cur]

            if cur in snake:
                cur = snake[cur]

            if not visited[cur]:
                visited[cur] = True
                q.append(cur)
                MAP[cur] = MAP[v] + 1

print(MAP[100])

