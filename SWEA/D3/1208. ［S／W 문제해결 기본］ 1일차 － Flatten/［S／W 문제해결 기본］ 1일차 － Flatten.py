# 1208. [S/W 문제해결 기본] 1일차 - Flatten

for t in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    for _ in range(N):
        max_h = max(lst)
        min_h = min(lst)

        if max_h - min_h <= 1:
            break

        max_idx = lst.index(max_h)
        min_idx = lst.index(min_h)

        lst[max_idx] -= 1
        lst[min_idx] += 1

    answer = max(lst) - min(lst)

    print(f"#{t} {answer}")