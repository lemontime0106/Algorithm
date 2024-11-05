N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
dp = [1] * N

lst.sort()

for i in range(1, N):
    for j in range(0, i):
        if lst[j][1] < lst[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))