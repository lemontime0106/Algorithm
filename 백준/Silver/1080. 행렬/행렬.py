N, M = map(int, input().split())
MAP = [list(map(int, list(input()))) for _ in range(N)]
answer = [list(map(int, list(input()))) for _ in range(N)]

def reverse(x, y):
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                MAP[i][j] = 1 - MAP[i][j]

cnt = 0
if N >= 3 and M >= 3:
    for i in range(N - 2):
        for j in range(M - 2):
            if MAP[i][j] != answer[i][j]:
                reverse(i, j)
                cnt += 1

if MAP != answer:
    cnt = -1

print(cnt)
