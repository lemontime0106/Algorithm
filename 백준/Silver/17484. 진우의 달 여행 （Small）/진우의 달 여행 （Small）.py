N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

dp = [[[float("inf")] * 3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    for d in range(3):
        dp[0][j][d] = MAP[0][j]

dx = [-1, 0, 1]

for i in range(1, N):
    for j in range(M):
        for d in range(3):
            prev_j = j - dx[d]
            if 0 <= prev_j < M:
                for prev_d in range(3):
                    if prev_d == d:
                        continue
                    dp[i][j][d] = min(dp[i][j][d], dp[i-1][prev_j][prev_d] + MAP[i][j])

answer = float("inf")
for j in range(M):
    answer = min(answer, min(dp[N-1][j]))
print(answer)
