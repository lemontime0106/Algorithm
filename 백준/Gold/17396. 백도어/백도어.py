import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

lst = list(map(int, input().split()))
lst[-1] = 0

for _ in range(M):
    a, b, t = map(int, input().split())

    graph[a].append((b, t))
    graph[b].append((a, t))

def dijkstra(start, end):
    distance = [float("inf")] * N
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        time, node = heapq.heappop(q)

        if time > distance[node]:
            continue

        for next_node, next_time in graph[node]:
            if distance[next_node] > distance[node] + next_time and not lst[next_node]:
                distance[next_node] = distance[node] + next_time
                heapq.heappush(q, (distance[next_node], next_node))

    return distance[end]

answer = dijkstra(0, N-1)

if answer == float("inf"):
    print(-1)
else:
    print(answer)
