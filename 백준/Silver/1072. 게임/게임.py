X, Y = map(int, input().split())
Z = (100 * Y) // X

left, right = 0, X
answer = 0

if Z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        if (Y + mid) * 100 // (X + mid) > Z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)