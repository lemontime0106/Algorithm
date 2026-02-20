import heapq

N, M = map(int, input().split())
A, B, C = map(int, input().split())

MAP = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    MAP[a].append((b, c))
    MAP[b].append((a, c))

def dijkstra(start, visited):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if cost > visited[now]:
            continue

        for nxt, weight in MAP[now]:
            new_cost = cost + weight

            if new_cost < visited[nxt]:
                visited[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))
    
    return visited

visitedA = dijkstra(A, [float("inf")] * (N+1))
visitedB = dijkstra(B, [float("inf")] * (N+1))
visitedC = dijkstra(C, [float("inf")] * (N+1))

answer = 0

for i in range(1, N+1):
    closest = min(visitedA[i], visitedB[i], visitedC[i])
    if closest != float("inf"):
        answer = max(answer, closest)

print(answer)