N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

maxK = 0
for i in range(N):
    for j in range(M):
        maxK = max(maxK, MAP[i][j])

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, target):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        for dx, dy in direct:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and MAP[nx][ny] > target:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

best_k = 1
best_cnt = 0

for k in range(1, maxK + 1):
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and MAP[i][j] > k:
                dfs(i, j, k)
                cnt += 1

    if cnt > best_cnt:
        best_cnt = cnt
        best_k = k

print(best_k, best_cnt)
