N, M = map(int, input().split())
lst = list(int(input()) for _ in range(N))
left, right = min(lst), sum(lst)

while left <= right:
    mid = (left + right) // 2
    cur = mid
    cnt = 1

    for i in range(N):
        if cur < lst[i]:
            cur = mid
            cnt += 1
        cur -= lst[i]

    if cnt > M or mid < max(lst):
        left = mid + 1
    else:
        right = mid - 1
        k = mid

print(k)