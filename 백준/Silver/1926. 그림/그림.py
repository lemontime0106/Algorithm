from collections import deque

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

temp = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and MAP[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))

    return cnt

for i in range(N):
    for j in range(M):
        if not visited[i][j] and MAP[i][j] == 1:
            temp.append(bfs(i, j))

print(len(temp))
print(max(temp) if temp else 0)