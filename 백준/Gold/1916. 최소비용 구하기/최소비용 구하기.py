import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())

def dijkstra(graph, start):
    distance = [float("inf")] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            d = dist + next_dist
            if d < distance[next_node]:
                distance[next_node] = d
                heapq.heappush(q, [d, next_node])
    return distance

answer = dijkstra(graph, start)
print(answer[end])

