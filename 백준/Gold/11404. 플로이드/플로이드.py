N = int(input())
M = int(input())

MAP = [[float("inf")] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    MAP[i][i] = 0

for i in range(M):
    a, b, fuel = map(int, input().split())
    MAP[a][b] = min(MAP[a][b], fuel)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                MAP[i][j] = 0
            else:
                MAP[i][j] = min((MAP[i][k] + MAP[k][j]), MAP[i][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if MAP[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(MAP[i][j], end=" ")
    print()


