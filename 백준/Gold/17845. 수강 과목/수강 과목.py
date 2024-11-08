N, K = map(int, input().split())
subjects = [[0, 0]]

for _ in range(K):
    a, b = map(int, input().split())
    subjects.append([a, b])

dp = [[0] * (N+1) for _ in range(K+1)]

for i in range(1, K+1):
    score = subjects[i][0]
    weight = subjects[i][1]

    for j in range(1, N+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], score + dp[i-1][j-weight])

print(dp[K][N])