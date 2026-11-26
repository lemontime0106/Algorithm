N, M = map(int, input().split())

lst = [int(input()) for _ in range(N)]

left, right = max(lst), sum(lst)

answer = 0

while left <= right:
    mid = (left + right) // 2

    temp = mid
    cnt = 1

    for money in lst:
        if temp < money:
            cnt += 1
            temp = mid

        temp -= money

    if cnt <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)