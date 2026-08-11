for t in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))

    diff = float("inf")
    answer = 0

    for i in range(1, N):
        left = sum(lst[:i])
        right = sum(lst[i:])

        d = abs(left - right)

        if d < diff:
            diff = d
            answer = i

    print(f"#{t} {answer} {diff}")