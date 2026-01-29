N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[0] * N for _ in range(N)]

def dfs(x, y):
    if visited[x][y] != 0:
        return visited[x][y]

    visited[x][y] = 1

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if MAP[x][y] < MAP[nx][ny]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)

    return visited[x][y]


answer = 0

for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))

print(answer)
