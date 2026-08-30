# 26925. 걷기 앱 기간 활동량 차이

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    current = sum(arr[:M])

    max_sum = current
    min_sum = current

    for i in range(M, N):
        current -= arr[i - M]
        current += arr[i]

        max_sum = max(max_sum, current)
        min_sum = min(min_sum, current)

    print(f"#{t} {max_sum - min_sum}")