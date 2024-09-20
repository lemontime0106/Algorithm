N = int(input())
sad = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

dp = [[0] * 101 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 101):
        if sad[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], happy[i] + dp[i-1][j-sad[i]])

print(dp[N][99])