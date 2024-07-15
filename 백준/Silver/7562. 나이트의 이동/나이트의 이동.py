from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    start = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    MAP = [[0] * N for _ in range(N)]
    direct = [(-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    q = deque()
    q.append((start[0], start[1]))
    while q:
        x, y = q.popleft()
        if x == goal[0] and y == goal[1]:
            print(MAP[x][y])
            break

        for d in direct:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and not MAP[nx][ny]:
                MAP[nx][ny] = MAP[x][y] + 1
                q.append((nx, ny))

