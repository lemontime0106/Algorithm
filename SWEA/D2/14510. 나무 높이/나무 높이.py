# 14510. 나무 높이

for t in range(1, int(input())+1):
    N = int(input())
    trees = list(map(int, input().split()))

    max_h = max(trees)

    one, two = 0, 0

    for h in trees:
        diff = max_h - h

        one += diff % 2
        two += diff // 2

    def possible(day):
        odd_days = (day + 1) // 2
        even_days = day // 2

        if one > odd_days:
            return False

        lack = max(0, two - even_days)

        needed_one = one + lack * 2

        return needed_one <= odd_days

    left = 0
    right = sum(max_h - h for h in trees) * 2

    while left < right:
        mid = (left + right) // 2

        if possible(mid):
            right = mid
        else:
            left = mid + 1

    print(f"#{t} {left}")