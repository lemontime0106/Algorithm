from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

start = []

for _ in range(M):
    start.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and MAP[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True

for s in start:
    i, j = s
    bfs(i-1, j-1)

answer = 0

for v in visited:
    for i in v:
        if i:
            answer += 1

print(answer)