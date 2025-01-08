from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

answer = 0
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ice = []
for i in range(N):
    for j in range(M):
        if MAP[i][j]:
            ice.append((i, j))

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    sea = []

    while q:
        x, y = q.popleft()
        s = 0

        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not MAP[nx][ny]:
                    s += 1
                elif MAP[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

        if s > 0:
            sea.append((x, y, s))

    for x, y, s in sea:
        MAP[x][y] = max(0, MAP[x][y] - s)

    return 1

while ice:
    visited = [[False] * M for _ in range(N)]
    temp = []
    group = 0
    for i, j in ice:
        if MAP[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if not MAP[i][j]:
            temp.append((i, j))

    if group > 1:
        print(answer)
        break

    ice = sorted(list(set(ice) - set(temp)))
    answer += 1

if group < 2:
    print(0)
