N = int(input())
lst = list(map(int, input().split()))
X = int(input())
lst.sort()

left, right = 0, N - 1
cnt = 0

while left < right:
    sum_nums = lst[left] + lst[right]

    if sum_nums == X:
        cnt += 1
        left += 1

    elif sum_nums < X:
        left += 1

    else:
        right -= 1

print(cnt)