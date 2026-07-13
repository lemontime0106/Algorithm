T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())

    maximum = max(X, Y, Z)

    if [X, Y, Z].count(maximum) == 1:
        print(-1, -1, -1)
    else:
        A = min(X, Z)
        B = min(X, Y)
        C = min(Y, Z)

        print(A, B, C)