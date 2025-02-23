from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]

answer = 0

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and MAP[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])

    return 1

for i in range(N):
    for j in range(M):
        if MAP[i][j] and not visited[i][j]:
            answer += bfs(i, j)

print(answer)