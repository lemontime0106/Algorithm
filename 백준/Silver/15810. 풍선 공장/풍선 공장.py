N, M = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 1, max(lst) * M
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in lst:
        total += int(mid / i)

    if total < M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)