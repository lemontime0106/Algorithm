N, M = map(int, input().split())

lst = []

for _ in range(M):
    lst.append(int(input()))

left, right = 1, max(lst)
answer = max(lst)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in lst:
        cnt += (i + mid - 1) // mid

    if cnt <= N:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
