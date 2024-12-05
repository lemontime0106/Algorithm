from collections import deque

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]

answer = [0, 0]  # [양의 수, 늑대의 수]
visited = [[False] * M for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    sheep = 0
    wolf = 0

    if MAP[x][y] == "k":
        sheep += 1
    elif MAP[x][y] == "v":
        wolf += 1

    while q:
        x, y = q.popleft()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and MAP[nx][ny] != "#":
                visited[nx][ny] = True
                if MAP[nx][ny] == "k":
                    sheep += 1
                elif MAP[nx][ny] == "v":
                    wolf += 1
                q.append((nx, ny))

    if sheep > wolf:
        answer[0] += sheep
    else:
        answer[1] += wolf

for i in range(N):
    for j in range(M):
        if not visited[i][j] and MAP[i][j] != "#":
            bfs(i, j)

print(*answer)
