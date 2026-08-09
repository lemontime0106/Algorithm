# 1249. [S/W 문제해결 응용] 4일차 - 보급로

import heapq

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

    INF = float("inf")
    visited = [[INF] * N for _ in range(N)]

    q = []
    heapq.heappush(q, (0, 0, 0))
    visited[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if cost > visited[x][y]:
            continue

        if x == N-1 and y == N-1:
            break

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + MAP[nx][ny]

                if new_cost < visited[nx][ny]:
                    visited[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

    print(f"#{t} {visited[N-1][N-1]}")