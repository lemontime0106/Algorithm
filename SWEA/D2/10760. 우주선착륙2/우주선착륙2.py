# 10760. 우주선착륙2

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    direct = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    answer = 0

    for x in range(N):
        for y in range(M):
            cnt = 0

            for dx, dy in direct:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < M:
                    if MAP[nx][ny] < MAP[x][y]:
                        cnt += 1

            if cnt >= 4:
                answer += 1

    print(f"#{t} {answer}")