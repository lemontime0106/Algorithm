from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[-1] * N for _ in range(N)]

q = deque()

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            q.append((i, j))
            visited[i][j] = 0

while q:
    x, y = q.popleft()

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == -1 and MAP[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

for i in range(N):
    for j in range(N):
        if visited[i][j] == -1 and MAP[i][j] == 1:
            visited[i][j] = -2

for i in visited:
    print(*i)