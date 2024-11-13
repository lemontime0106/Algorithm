import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

# 초기 조건 세팅 (길이 1과 2의 회문)
for i in range(N):
    dp[i][i] = 1
for i in range(N - 1):
    if lst[i] == lst[i + 1]:
        dp[i][i + 1] = 1

# 길이가 3 이상인 경우의 회문 검사
for length in range(3, N + 1): # 길이 3부터 N까지
    for i in range(N - length + 1):
        j = i + length - 1
        if lst[i] == lst[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])
