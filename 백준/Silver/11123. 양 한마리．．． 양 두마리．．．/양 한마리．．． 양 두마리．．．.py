from collections import deque

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and MAP[nx][ny] == "#":
                q.append([nx, ny])
                visited[nx][ny] = True

for _ in range(int(input())):
    N, M = map(int, input().split())
    MAP = [list(input()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == "#" and not visited[i][j]:
                bfs(i, j)
                answer += 1

    print(answer)