from collections import deque

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

virus = []
for i in range(N):
    for j in range(N):
        if MAP[i][j]:
            virus.append((MAP[i][j], 0, i, j))    # virus, sec, x, y

virus.sort()
q = deque(virus)

while q:
    v, s, x, y = q.popleft()
    if s == S:
        break

    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if not MAP[nx][ny]:
                MAP[nx][ny] = v
                q.append((v, s+1, nx, ny))

print(MAP[X-1][Y-1])