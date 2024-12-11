N = int(input())
M = int(input())
lst = list(map(int, input().split()))

lst.sort()
left, right = 0, N-1
answer = 0

while left < right:
    mid = lst[left] + lst[right]

    if mid < M:
        left += 1
    elif mid > M:
        right -= 1
    else:
        answer += 1
        left += 1
        right -= 1

print(answer)