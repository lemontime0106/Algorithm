for _ in range(int(input())):
    N = int(input())

    for i in [25, 10, 5, 1]:
        print(N // i, end=" ")
        N = N % i

    print()