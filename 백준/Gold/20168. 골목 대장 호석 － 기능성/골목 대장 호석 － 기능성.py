import heapq

N, M, start, end, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [float("inf")] * (N+1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, 0, s))  # (total_cost, max_cost, current_node)
    dist[s] = 0

    while q:
        total_cost, max_cost, now = heapq.heappop(q)

        if total_cost > C:
            continue

        if now == end:  # 목적지에 도달하면 max_cost 반환
            return max_cost

        for next_node, next_cost in graph[now]:
            cost = total_cost + next_cost
            if cost > C:
                continue

            if cost < dist[next_node]:  # 더 작은 비용으로 도달 가능할 때만 진행
                dist[next_node] = cost
                heapq.heappush(q, (cost, max(max_cost, next_cost), next_node))

    return -1  # 경로를 찾지 못한 경우

result = dijkstra(start)
print(result)
