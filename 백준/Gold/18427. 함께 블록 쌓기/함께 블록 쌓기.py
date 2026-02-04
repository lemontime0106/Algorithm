N, M, H = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (H+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    temp = lst[i-1]
    for h in range(H+1):
        dp[i][h] = dp[i-1][h]

        for t in temp:
            if h >= t:
                dp[i][h] = (dp[i][h] + dp[i-1][h-t]) % 10007

print(dp[N][H] % 10007)