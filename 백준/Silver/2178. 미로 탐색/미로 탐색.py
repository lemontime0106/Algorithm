from collections import deque

N, M = map(int, input().split())

MAP = [list(map(int, input().strip())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] == 1:
                MAP[nx][ny] = MAP[x][y] + 1
                q.append((nx, ny))

    return MAP[N-1][M-1]

print(bfs(0, 0))
