# 12712. 파리퇴치3

ten = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cross = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

def solution(x, y, size, MAP):
    N = len(MAP)

    t, c = MAP[x][y], MAP[x][y]

    for i in range(1, size):
        for dx, dy in ten:
            nx, ny = x + dx * i, y + dy * i

            if 0 <= nx < N and 0 <= ny < N:
                t += MAP[nx][ny]

        for dx, dy in cross:
            nx, ny = x + dx * i, y + dy * i

            if 0 <= nx < N and 0 <= ny < N:
                c += MAP[nx][ny]

    return max(t, c)



for t in range(1, int(input())+1):
    N, M = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for x in range(N):
        for y in range(N):
            answer = max(answer, solution(x, y, M, MAP))

    print(f"#{t} {answer}")