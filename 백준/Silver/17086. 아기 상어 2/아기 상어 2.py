from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
counter = [[-1] * M for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def bfs(x, y, visited):
    cnt = 0
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        x, y, dist = q.popleft()

        if MAP[x][y] == 1:
            return dist

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return -1


for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            visited = [[False] * M for _ in range(N)]
            counter[i][j] = bfs(i, j, visited)
        else:
            counter[i][j] = 0

answer = 0

for row in counter:
    for r in row:
        answer = max(answer, r)

print(answer)