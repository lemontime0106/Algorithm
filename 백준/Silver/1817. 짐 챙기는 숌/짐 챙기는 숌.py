N, M = map(int, input().split())

if N == 0:
    print(0)
else:
    lst = list(map(int, input().split()))

    weight = 0
    answer = 0
    for i in lst:
        weight += i

        if weight == M:
            answer += 1
            weight = 0

        elif weight > M:
            weight = i
            answer += 1
    if weight:
        answer += 1

    print(answer)

