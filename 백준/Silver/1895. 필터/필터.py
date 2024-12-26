N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

T = int(input())

answer = 0

direct = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1), (0, 0)]

for i in range(1, N-1):
    for j in range(1, M-1):
        temp = []
        for dx, dy in direct:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < M:
                temp.append(MAP[nx][ny])

        temp.sort()

        if temp[4] >= T:
            answer += 1

print(answer)
