# 1954. 달팽이 숫자

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, int(input())+1):
    N = int(input())

    MAP = [[0] * N for _ in range(N)]

    x, y = 0, 0
    d = 0

    for i in range(1, N*N+1):
        MAP[x][y] = i

        nx, ny = x + dx[d], y + dy[d]

        if (0 <= nx < N and 0 <= ny < N and MAP[nx][ny] == 0):
            x, y = nx, ny

        else:
            d = (d+1) % 4

            x += dx[d]
            y += dy[d]

    print(f"#{t}")

    for row in MAP:
        print(*row)