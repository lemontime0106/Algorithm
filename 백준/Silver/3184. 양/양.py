from collections import deque

N, M = map(int, input().split())

MAP = [list(input()) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited = [[False] * M for _ in range(N)]
answer = [0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    visited[y][x] = True
    sheep, wolf = 0, 0

    if MAP[y][x] == "o":
        sheep += 1
    elif MAP[y][x] == "v":
        wolf += 1

    while q:
        x, y = q.popleft()
        for d in direct:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < M and 0 <= ny < N and MAP[ny][nx] != "#" and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True

                if MAP[ny][nx] == "o":
                    sheep += 1
                elif MAP[ny][nx] == "v":
                    wolf += 1

    return (sheep, wolf)

for i in range(N):
    for j in range(M):
        if MAP[i][j] != "#" and not visited[i][j]:
            sheep, wolf = bfs(j, i)

            if sheep > wolf:
                wolf = 0
            else:
                sheep = 0

            answer[0] += sheep
            answer[1] += wolf

print(*answer)
