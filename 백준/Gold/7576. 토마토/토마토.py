from collections import deque

M, N = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
tomato = []

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            tomato.append((i, j))
            visited[i][j] = 0
        elif MAP[i][j] == -1:
            visited[i][j] = -1

q = deque(tomato)

while q:
    x, y = q.popleft()
    for d in direct:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and not MAP[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

flag = True
answer = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0 and visited[i][j] == -1:
            flag = False
        if visited[i][j] > answer:
            answer = visited[i][j]

if flag:
    print(answer)
else:
    print(-1)


