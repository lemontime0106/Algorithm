N = int(input())
stair = [int(input()) for _ in range(N)]
dp = [0] * N

if len(stair) <= 2:
    print(sum(stair))

else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[-1])