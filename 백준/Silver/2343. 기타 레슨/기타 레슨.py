N, M = map(int, input().split())

lst = list(map(int, input().split()))

left, right = max(lst), sum(lst)
answer = right

while left <= right:
    mid = (left + right) // 2
    cnt = 1

    temp = 0
    for i in lst:
        if temp + i > mid:
            cnt += 1
            temp = i
        else:
            temp += i

    if cnt <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)