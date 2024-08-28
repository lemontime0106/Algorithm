N, M = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(int(input()))

left, right = 1, max(lst) * M
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for l in lst:
        cnt += mid // l

        if cnt == M:
            break

    if cnt >= M:
        answer = mid
        right = mid - 1

    else:
        left = mid + 1

print(answer)