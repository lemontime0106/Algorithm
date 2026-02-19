import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, N+1):
    graph[i].sort()

start, end = map(int, input().split())

INF = float("inf")
dist = [INF] * (N+1)

def dijkstra():
    pq = []
    heapq.heappush(pq, (0, [start], start))
    dist[start] = 0

    while pq:
        cost, path, now = heapq.heappop(pq)

        if now == end:
            return cost, path

        if cost > dist[now]:
            continue

        for nxt, weight in graph[now]:
            new_cost = cost + weight

            if new_cost <= dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, path + [nxt], nxt))

    return INF, []

ans_cost, ans_path = dijkstra()

print(ans_cost)
print(*ans_path)
