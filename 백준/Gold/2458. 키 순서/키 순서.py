N, M = map(int, input().split())
MAP = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    MAP[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if MAP[i][k] == 1 and MAP[k][j] == 1:
                MAP[i][j] = 1

answer = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        cnt += MAP[i][j]
        cnt += MAP[j][i]
    if cnt == N-1:
        answer += 1

print(answer)