import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    distance = [float("inf")] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)
        if cost > distance[node]:
            continue

        for next_node, next_cost in graph[node]:
            total = cost + next_cost
            if total < distance[next_node]:
                distance[next_node] = total
                heapq.heappush(q, (total, next_node))
    return distance

distance_from_x = dijkstra(X)

max_distance = 0
for i in range(1, N + 1):
    if i != X:
        distance_to_x = dijkstra(i)[X]
        total_distance = distance_from_x[i] + distance_to_x
        max_distance = max(max_distance, total_distance)

print(max_distance)
