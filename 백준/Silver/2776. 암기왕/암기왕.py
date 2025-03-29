for _ in range(int(input())):
    N = int(input())
    memo1 = list(map(int, input().split()))
    M = int(input())
    memo2 = list(map(int, input().split()))

    memoMap = dict()

    for i in range(N):
        if memo1[i] in memoMap:
            memoMap[memo1[i]] += 1
        else:
            memoMap[memo1[i]] = 1

    for i in range(M):
        if memo2[i] in memoMap:
            print(1)
        else:
            print(0)