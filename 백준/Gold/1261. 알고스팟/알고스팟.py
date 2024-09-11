import heapq

N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(M)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distance = [[float("inf")] * N for _ in range(M)]
distance[0][0] = 0
q = []
heapq.heappush(q, (MAP[0][0], 0, 0))

while q:
    d, x, y = heapq.heappop(q)

    if x == N-1 and y == M-1:
        print(d)
        break

    for i in direct:
        nx, ny = x + i[0], y + i[1]
        if 0 <= nx < N and 0 <= ny < M:
            cost = d + MAP[ny][nx]
            if cost < distance[ny][nx]:
                distance[ny][nx] = cost
                heapq.heappush(q, (cost, nx, ny))
