import heapq

for t in range(1, int(input())+1):
    N, E = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        a, b, c = map(int, input().split())

        graph[a].append((b, c))

    INF = float("inf")
    dist = [INF] * (N+1)

    dist[0] = 0

    q = []
    heapq.heappush(q, (0, 0))

    while q:
        d, node = heapq.heappop(q)

        if dist[node] < d:
            continue

        if node == N:
            break

        for next_node, cost in graph[node]:
            new_dist = cost + d

            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    print(f"#{t} {dist[N]}")