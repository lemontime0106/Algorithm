import heapq
A, B = map(int, input().split())
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [float("inf")] * (N+1)
dist[A] = 0

q = []
heapq.heappush(q, (0, A))

while q:
    cost, node = heapq.heappop(q)
    if cost > dist[node]:
        continue

    for next in graph[node]:
        if dist[next] > cost + 1:
            dist[next] = cost + 1
            heapq.heappush(q, (cost + 1, next))

if dist[B] == float("inf"):
    print(-1)
else:
    print(dist[B])
