N, K = map(int, input().split())

dp = [0]
for i in range(2, N+2):
    dp.append([0] * i)

dp[1] = [1, 1]

for i in range(2, N):
    dp[i][0] = 1
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
    dp[i][-1] = 1

if K == 0 or K == N:
    print(1)
else:
    print((dp[N-1][K-1] + dp[N-1][K]) % 10007)