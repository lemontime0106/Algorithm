from collections import deque

N, M = map(int, input().split())

MAP = []

for i in range(N):
    a = input()
    lst = []
    for t in a:
        lst.append(int(t))
    MAP.append(lst)

q = deque()
q.append((0, 0, 0))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

direct = [(0, -1), (0, 1), (1, 0), (-1, 0)]

while q:
    x, y, broken = q.popleft()

    if x == N - 1 and y == M - 1:
        print(visited[x][y][broken])
        break

    for d in direct:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == 1 and broken == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))
            elif MAP[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                visited[nx][ny][broken] = visited[x][y][broken] + 1
                q.append((nx, ny, broken))
else:
    if visited[N - 1][M - 1][0] == 0 and visited[N - 1][M - 1][1] == 0:
        print(-1)
