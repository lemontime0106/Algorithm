import heapq

N, M = map(int, input().split())
MAP = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    MAP[b].append((a, c))

visited = [float("inf")] * (N+1)

def solution(start):
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
                heapq.heappush(q, (new_cost, nxt))

solution(N)

print(max(visited[1:N]))