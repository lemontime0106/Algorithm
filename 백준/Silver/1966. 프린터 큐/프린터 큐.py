for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    answer = 1

    while lst:
        if lst[0] < max(lst):
            lst.append(lst.pop(0))

        else:
            if M == 0:
                break

            lst.pop(0)
            answer += 1

        if M > 0:
            M -= 1
        else:
            M = len(lst) - 1
    print(answer)