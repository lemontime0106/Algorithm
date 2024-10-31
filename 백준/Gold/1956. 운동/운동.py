V, E = map(int, input().split())
MAP = [[float("inf")] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    MAP[a][b] = c


distance = [float("inf")] * (V+1)

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if MAP[i][k] + MAP[k][j] < MAP[i][j]:
                MAP[i][j] = MAP[i][k] + MAP[k][j]

answer = float("inf")

for i in range(1, V+1):
    answer = min(answer, MAP[i][i])

if answer == float("inf"):
    print(-1)
else:
    print(answer)