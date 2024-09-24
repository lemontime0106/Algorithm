import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [float("inf")] * (N+1)

q = []
heapq.heappush(q, (0, 1))
dist[1] = 0

while q:
    d, now = heapq.heappop(q)

    if d > dist[now]:
        continue

    for nn, nd in graph[now]:
        cost = d + nd
        if cost < dist[nn]:
            dist[nn] = cost
            heapq.heappush(q, (cost, nn))

print(dist[N])
