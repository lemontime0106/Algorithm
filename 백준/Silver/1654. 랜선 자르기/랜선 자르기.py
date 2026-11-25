K, N = map(int, input().split())

lst = []

for _ in range(K):
    lst.append(int(input()))

max_lst = max(lst)

left, right = 1, max_lst
answer = 0

while left <= right:
    mid = (left + right) // 2

    cnt = 0

    for l in lst:
        cnt += l // mid

    if cnt >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid -1

print(answer)