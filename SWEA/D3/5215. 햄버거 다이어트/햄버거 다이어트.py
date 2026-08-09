# 5215. 햄버거 다이어트

for t in range(1, int(input())+1):
    N, L = map(int, input().split())

    dp = [0] * (L+1)

    for _ in range(N):
        score, cal = map(int, input().split())

        for c in range(L, cal-1, -1):
            dp[c] = max(dp[c], dp[c-cal]+score)

    print(f"#{t} {dp[L]}")