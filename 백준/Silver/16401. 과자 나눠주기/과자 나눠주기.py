N, M = map(int, input().split())

lst = list(map(int, input().split()))

left, right = 1, max(lst)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in lst:
        if i >= mid:
            cnt += (i // mid)

    if cnt >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)