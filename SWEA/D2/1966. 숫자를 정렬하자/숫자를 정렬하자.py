# 1966. 숫자를 정렬하자

for t in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i

        for j in range(i + 1, N):
            if lst[j] < lst[min_idx]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    print(f"#{t}", *lst)