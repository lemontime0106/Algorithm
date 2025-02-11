import heapq

V, E, P = map(int, input().split())

distance = [float("inf")] * (V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    distance = [float("inf")] * (V+1)
    distance[start] = 0

    while heap:
        cost, curr = heapq.heappop(heap)
        for next, c in graph[curr]:
            total = cost + c

            if distance[next] > total:
                distance[next] = total
                heapq.heappush(heap, [total, next])
    return distance

# 거리가 같다 => 최단거리 경로와 같다. 즉 만난다!
if dijkstra(1)[V] == dijkstra(1)[P] + dijkstra(P)[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")