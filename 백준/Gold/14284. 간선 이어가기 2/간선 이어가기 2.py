import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, input().split())

q = []
answer = [float("inf")] * (N+1)
answer[start] = 0
heapq.heappush(q, (start, 0))

while q:
    node, cost = heapq.heappop(q)

    if answer[node] < cost:
        continue

    for next_node, next_cost in graph[node]:
        total = next_cost + cost
        if total < answer[next_node]:
            answer[next_node] = total
            heapq.heappush(q, (next_node, total))

print(answer[end])