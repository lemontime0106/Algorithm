N, M = map(int, input().split())
MAP = [input() for _ in range(N)]

answer = []

for i in range(N-7):
    for j in range(M-7):
        wcnt, bcnt = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if MAP[a][b] != "W":
                        wcnt += 1
                    if MAP[a][b] != "B":
                        bcnt += 1

                else:
                    if MAP[a][b] != "B":
                        wcnt += 1
                    if MAP[a][b] != "W":
                        bcnt += 1
        answer.append(min(wcnt, bcnt))
print(min(answer))
