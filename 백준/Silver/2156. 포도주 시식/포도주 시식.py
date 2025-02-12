N = int(input())

lst = [int(input()) for _ in range(N)]

dp = [0] * (N if N > 2 else 3)

if N == 1:
    print(lst[0])
elif N == 2:
    print(lst[0] + lst[1])
else:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[0] + lst[2], lst[1] + lst[2], dp[1])

    for i in range(3, N):
        # 현재값 포함 + 하나 건너뜀, 현재값, 직전값 + 두칸 건너뜀, 현재값 X
        dp[i] = max(lst[i] + dp[i-2], lst[i] + lst[i-1] + dp[i-3], dp[i-1])

    print(max(dp))