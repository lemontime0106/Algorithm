N, M = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(int(input()))

left, right = 1, max(lst)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in lst:
        cnt += i // mid

    if cnt >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)