# 25052. 등산로

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for i in range(N):
        for j in range(N):
            x, y = i, j
            cnt = 1

            while True:
                next_x = -1
                next_y = -1
                min_height = 101

                for dx, dy in direct:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < N and 0 <= ny < N:
                        if MAP[nx][ny] < MAP[x][y] and MAP[nx][ny] < min_height:
                            min_height = MAP[nx][ny]
                            next_x = nx
                            next_y = ny

                if next_x == -1:
                    break

                x, y = next_x, next_y
                cnt += 1

            answer = max(answer, cnt)

    print(f"#{t} {answer}")