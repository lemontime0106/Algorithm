N, M = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

MAX_COST = sum(cost)
dp = [0] * (MAX_COST + 1)

for i in range(N):
    m = memory[i]
    c = cost[i]
    for j in range(MAX_COST, c-1, -1):
        dp[j] = max(dp[j], dp[j-c] + m)

for i in range(MAX_COST+1):
    if dp[i] >= M:
        print(i)
        break