from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j):
    q = deque()
    q.append((i, j))

    visited[i][j] = 0

    while q:
        x, y = q.popleft()

        for d in direct:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if MAP[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif MAP[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()