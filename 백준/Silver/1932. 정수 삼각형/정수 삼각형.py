N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]

dp = []
for i in range(1, N+1):
    temp = [0] * i
    dp.append(temp)

dp[0][0] = MAP[0][0]

for i in range(1, N):
    for j in range(len(dp[i])):
        if j != 0 and j != (len(dp[i]) - 1):
            dp[i][j] = max(MAP[i][j] + dp[i-1][j-1], MAP[i][j] + dp[i-1][j])
        elif j == 0:
            dp[i][j] = MAP[i][j] + dp[i-1][0]
        else:
            dp[i][j] = MAP[i][j] + dp[i-1][-1]

print(max(dp[-1]))


