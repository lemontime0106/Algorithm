N = int(input())
MAP = [[N] * N for _ in range(N)]
dist = [0] * N

for i in range(N):
    for j in range(N):
        if i == j:
            MAP[i][j] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    MAP[a-1][b-1], MAP[b-1][a-1] = 1, 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

for i in range(N):
    dist[i] = max(MAP[i])

answer = min(dist)

print(answer, dist.count(answer))
[print(i+1, end=" ") if dist[i] == answer else None for i in range(N)]