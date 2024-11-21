from collections import deque

R, C, N = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

q = deque()

for i in range(R):
    for j in range(C):
        if MAP[i][j] == "O":
            q.append([i, j])

t = 1

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while t < N:
    for i in range(R):
        for j in range(C):
            if MAP[i][j] == ".":
                MAP[i][j] = "O"

    t += 1
    if t == N:
        break

    while q:
        x, y = q.popleft()
        MAP[x][y] = "."

        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                MAP[nx][ny] = "."

    for i in range(R):
        for j in range(C):
            if MAP[i][j] == "O":
                q.append([i, j])
    t += 1

for m in MAP:
    print("".join(m))