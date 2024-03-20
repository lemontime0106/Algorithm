N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = []
    q.append((x, y))
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + direct[i][0]
            ny = y + direct[i][1]
            if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] == 1:
                MAP[nx][ny] = MAP[x][y] + 1
                q.append((nx, ny))

    return MAP[N-1][M-1]

print(bfs(0, 0))