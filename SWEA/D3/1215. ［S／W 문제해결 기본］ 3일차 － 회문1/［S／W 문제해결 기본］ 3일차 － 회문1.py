# 1215. [S/W 문제해결 기본] 3일차 - 회문1

for t in range(1, 11):
    N = int(input())
    MAP = [input() for _ in range(8)]

    answer = 0

    for i in range(8):
        for j in range(8 - N + 1):
            word = MAP[i][j:j+N]

            if word == word[::-1]:
                answer += 1

    for j in range(8):
        for i in range(8-N+1):
            word = ""

            for k in range(N):
                word += MAP[i+k][j]

            if word == word[::-1]:
                answer += 1

    print(f"#{t} {answer}")