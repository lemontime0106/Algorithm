N = int(input())

for _ in range(N):
    tree = int(input())
    lst = list(map(int, input().split()))

    lst.sort()

    answer = 0

    for i in range(2, tree):
        answer = max(answer, abs(lst[i] - lst[i-2]))
    print(answer)