T = int(input())

for _ in range(T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(2)]

    if N > 1:
        MAP[0][1] += MAP[1][0]
        MAP[1][1] += MAP[0][0]
    for i in range(2, N):
        MAP[0][i] += max(MAP[1][i-1], MAP[1][i-2])
        MAP[1][i] += max(MAP[0][i-1], MAP[0][i-2])

    print(max(MAP[0][N-1], MAP[1][N-1]))

