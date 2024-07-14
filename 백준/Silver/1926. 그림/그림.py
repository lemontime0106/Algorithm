from collections import deque

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
lst = []
def bfs(x, y):
    cnt = 1

    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for d in direct:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and MAP[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return cnt

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1 and not visited[i][j]:
            a = bfs(i, j)
            lst.append(a)

if len(lst) == 0:
    print(0)
    print(0)
else:
    print(len(lst))
    print(max(lst))