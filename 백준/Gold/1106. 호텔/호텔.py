C, N = map(int, input().split())
lst = [[0, 0]]

for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])

dp = [float("inf")] * (C + 100)
dp[0] = 0

for i in range(1, N+1):
    cost = lst[i][0]
    people = lst[i][1]

    for j in range(people, C+100):
        dp[j] = min(dp[j], dp[j-people] + cost)

print(min(dp[C:]))