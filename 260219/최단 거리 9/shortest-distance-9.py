import heapq

N, M = map(int, input().split())

MAP = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    MAP[a].append((b, c))
    MAP[b].append((a, c))

visited = [float("inf")] * (N+1)
prev = [0] * (N+1)

A, B = map(int, input().split())

def dijsktra(start):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if cost > visited[now]:
            continue
        
        for nxt, weight in MAP[now]:
            new_cost = weight + cost

            if new_cost < visited[nxt]:
                visited[nxt] = new_cost
                prev[nxt] = now
                heapq.heappush(q, (new_cost, nxt))

dijsktra(A)

print(visited[B])

path = []
cur = B

while cur != 0:
    path.append(cur)
    cur = prev[cur]

path.reverse()
print(*path)