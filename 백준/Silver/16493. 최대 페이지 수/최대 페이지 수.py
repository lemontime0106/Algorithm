N, M = map(int, input().split())
lst = [[0, 0]]

for _ in range(M):
    lst.append(list(map(int, input().split())))

dp = [[0] * (N+1) for _ in range(M+1)]

for i in range(1, M+1):
    day = lst[i][0]
    page = lst[i][1]

    for j in range(1, N+1):
        if j < day:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], page + dp[i-1][j-day])

print(dp[M][N])