for _ in range(int(input())):
    J, N = map(int, input().split())
    lst = []

    for _ in range(N):
        a, b = map(int, input().split())
        lst.append(a * b)

    lst.sort(reverse=True)
    answer = 0

    for i in range(N):
        J -= lst[i]
        answer += 1
        if J <= 0:
            break

    print(answer)