import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
blank = set()
blank.add((1, 1))
for _ in range(K):
    a, b = map(int, input().split())
    blank.add((a, b))
MAP = [[0] * (M+1) for _ in range(N+2)]
MAP[1][1] = 1
for j in range(1, M+1):
    for i in range(1, N+1):
        if (i, j) in blank:
            continue

        if j % 2 == 0:
            MAP[i][j] = (MAP[i-1][j] + MAP[i][j-1] + MAP[i+1][j-1]) % (10 ** 9 + 7)
        elif j % 2 == 1:
            MAP[i][j] = (MAP[i-1][j] + MAP[i-1][j-1] + MAP[i][j-1]) % (10 ** 9 + 7)

print(MAP[N][M])