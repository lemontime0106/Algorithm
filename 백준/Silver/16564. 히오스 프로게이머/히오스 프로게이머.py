N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

left, right = min(lst), min(lst) + K
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for l in lst:
        if l < mid:
            cnt += mid - l

    if cnt <= K:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)


