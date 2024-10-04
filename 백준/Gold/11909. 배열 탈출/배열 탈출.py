N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i < 1 and j < 1:
            continue

        cost1, cost2 = float("inf"), float("inf")
        if i >= 1:
            cost1 = dp[i-1][j] + (0 if MAP[i][j] < MAP[i-1][j] else MAP[i][j] - MAP[i-1][j] + 1)

        if j >= 1:
            cost2 = dp[i][j-1] + (0 if MAP[i][j] < MAP[i][j-1] else MAP[i][j] - MAP[i][j-1] + 1)

        dp[i][j] = min(cost1, cost2)

print(dp[-1][-1])