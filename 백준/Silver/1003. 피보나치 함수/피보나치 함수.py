for _ in range(int(input())):
    N = int(input())
    a, b = 1, 0

    for i in range(N):
        a, b = b, a+b

    print(a, b)