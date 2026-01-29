import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[x][y] > MAP[nx][ny]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]


print(dfs(0, 0))

