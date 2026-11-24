from collections import deque

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

M, N = map(int ,input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

q = deque()

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            q.append((i, j))


def bfs(x, y):
    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                MAP[nx][ny] = MAP[x][y] + 1
                visited[nx][ny] = True

while q:
    x, y = q.popleft()
    bfs(x, y)

answer = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            print(-1)
            exit()

        answer = max(answer, MAP[i][j])

print(answer - 1)