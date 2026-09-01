# 27021. 용량별 상자로 나눠 담기 경우의 수

for t in range(1, int(input()) + 1):
    N, C = map(int, input().split())
    boxes = list(map(int, input().split()))

    # dp[i] = 합이 i가 되도록 상자를 사용하는 방법의 수
    dp = [0] * (N + 1)
    dp[0] = 1

    for box in boxes:
        for i in range(box, N + 1):
            dp[i] += dp[i - box]

    print(f"#{t} {dp[N]}")