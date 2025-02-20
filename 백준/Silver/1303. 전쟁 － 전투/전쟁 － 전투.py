from collections import deque

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    cnt = 1
    color = MAP[x][y]

    while q:
        x, y = q.popleft()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                if color == MAP[nx][ny]:
                    cnt += 1
                    q.append([nx, ny])
                    visited[nx][ny] = True

    return [color, cnt ** 2]

B = 0
W = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            color, power = bfs(i, j)
            if color == "B":
                B += power
            else:
                W += power

print(W, B)
