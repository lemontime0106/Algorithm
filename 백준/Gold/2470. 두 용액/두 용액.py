N = int(input())
lst = list(map(int, input().split()))
lst.sort()

left, right = 0, N-1

answer = [lst[left], lst[right]]
total = abs(lst[left] + lst[right])

while left < right:
    left_val = lst[left]
    right_val = lst[right]

    sum_val = left_val + right_val

    if abs(sum_val) < total:
        total = abs(sum_val)
        answer = [left_val, right_val]
        if total == 0:
            break
    if sum_val < 0:
        left += 1
    else:
        right -= 1

print(*answer)