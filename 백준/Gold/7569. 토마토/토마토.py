from collections import deque

M, N, H = map(int, input().split())

MAP = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
q = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

answer = 0

def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if MAP[nx][ny][nz] == 0 and not visited[nx][ny][nz]:
                    q.append((nx, ny, nz))
                    MAP[nx][ny][nz] = MAP[x][y][z] + 1
                    visited[nx][ny][nz] = True

for i in range(H):
    for j in range(N):
        for k in range(M):
            if MAP[i][j][k] == 1 and not visited[i][j][k]:
                q.append((i, j, k))
                visited[i][j][k] = True

bfs()

for i in MAP:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            answer = max(answer, k)

print(answer - 1)
