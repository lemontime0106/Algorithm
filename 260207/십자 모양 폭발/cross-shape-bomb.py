N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]

A, B = map(int, input().split())

A -= 1
B -= 1

size = MAP[A][B]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for dx, dy in direct:
    for i in range(size):
        nx, ny = A + dx * i, B + dy * i

        if 0 <= nx < N and 0 <= ny < N:
            MAP[nx][ny] = 0


for i in range(N):
    for _ in range(N):
        for j in range(N-1, 0, -1):
            if MAP[j][i] == 0 and MAP[j-1][i] != 0:
                MAP[j][i], MAP[j-1][i] = MAP[j-1][i], 0
                
for i in MAP:
    print(*i)
