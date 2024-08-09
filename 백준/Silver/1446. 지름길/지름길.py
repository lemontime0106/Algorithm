import heapq

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
distance = [float("inf")] * (D + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    a, b, c = map(int, input().split())
    if b > D:
        continue
    graph[a].append((b, c))

dijkstra(0)
print(distance[D])