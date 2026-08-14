# 20230. 풍선팡 보너스게임2

for t in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for x in range(N):
        for y in range(N):
            temp = 0

            for k in range(N):
                temp += MAP[x][k]
                temp += MAP[k][y]
            temp -= MAP[x][y]

            answer = max(answer, temp)

    print(f"#{t} {answer}")