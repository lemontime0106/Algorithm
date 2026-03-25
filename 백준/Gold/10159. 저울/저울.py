N = int(input())
M = int(input())

MAP = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    MAP[a][b] = True

for k in range(1, N+1):
    for i in range(1, N+1):
        if MAP[i][k]:
            for j in range(1, N+1):
                if MAP[k][j]:
                    MAP[i][j] = True

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if not MAP[i][j] and not MAP[j][i]:
            cnt += 1

    print(cnt)