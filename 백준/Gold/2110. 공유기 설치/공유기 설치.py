N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

left, right = 1, lst[-1]
answer = 0

while left <= right:
    mid = (left + right) // 2
    cur = lst[0]
    cnt = 1

    for i in range(1, len(lst)):
        if lst[i] >= cur + mid:
            cnt += 1
            cur = lst[i]

    if cnt >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)