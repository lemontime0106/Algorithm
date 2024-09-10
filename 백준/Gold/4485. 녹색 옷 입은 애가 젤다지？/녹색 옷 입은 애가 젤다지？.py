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
        q = []

        distance = [[float("inf")] * N for _ in range(N)]
        distance[0][0] = MAP[0][0]

        heapq.heappush(q, (MAP[0][0], 0, 0))

        while q:
            d, y, x = heapq.heappop(q)

            if y == N-1 and x == N-1:
                print(f"Problem {T}: {d}")
                break

            for i in direct:
                ny, nx = y + i[1], x + i[0]
                if 0 <= ny < N and 0 <= nx < N:
                    cost = d + MAP[ny][nx]
                    if  distance[ny][nx] > cost:
                        distance[ny][nx] = d + MAP[ny][nx]
                        heapq.heappush(q, (MAP[ny][nx] + d, ny, nx))