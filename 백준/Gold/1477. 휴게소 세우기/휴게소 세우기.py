N, M, L = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

left, right = 1, L
answer = float("inf")

while left <= right:
    mid = (left + right) // 2
    temp = lst[:]
    temp.append(0)
    temp.append(L)
    temp.sort()

    cnt = 0

    for i in range(len(temp) - 1):
        if temp[i+1] - temp[i] > mid:
            cnt += (temp[i+1] - temp[i] - 1) // mid

    if cnt > M:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
