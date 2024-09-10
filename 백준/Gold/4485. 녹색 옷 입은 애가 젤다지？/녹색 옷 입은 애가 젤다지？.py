import heapq

T = 0
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    N = int(input())
    if N == 0:
        break
    else:
        T += 1
        MAP = [list(map(int, input().split())) for _ in range(N)]
        distance = [[float("inf")] * N for _ in range(N)]
        distance[0][0] = MAP[0][0]
        q = []
        heapq.heappush(q, (MAP[0][0], 0, 0))

        while q:
            d, x, y = heapq.heappop(q)
            
            if x == N-1 and y == N-1:
                print(f"Problem {T}: {d}")
                break

            for i in direct:
                nx, ny = x + i[0], y + i[1]
                if 0 <= nx < N and 0 <= ny < N:
                    cost = d + MAP[nx][ny]
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(q, (cost, nx, ny))
