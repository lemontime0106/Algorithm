import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [float("inf")] * (N + 1)
    q = []
    distance[start] = 0
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

v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)
original_distance = dijkstra(1)

v1_cost = original_distance[v1] + v1_distance[v2] + v2_distance[N]
v2_cost = original_distance[v2] + v2_distance[v1] + v1_distance[N]

answer = min(v1_cost, v2_cost)
print(answer if answer < float("inf") else -1)