N = int(input())
lst = list(map(int, input().split()))
lst.sort()
M = int(input())
number = list(map(int, input().split()))

answer = []

for n in number:
    left, right = 0, N-1
    exist = False
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] > n:
            right = mid - 1
        elif lst[mid] < n:
            left = mid + 1
        else:
            exist = True
            break

    if exist:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)