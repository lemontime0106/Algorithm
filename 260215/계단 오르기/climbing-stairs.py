N = int(input())

if N == 1:
    print(0)
else:
    dp = [0] * (N+1)

    dp[0] = 1
    if N >= 2:
        dp[2] = 1
    if N >= 3:
        dp[3] = 1

    for i in range(4, N+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[N])