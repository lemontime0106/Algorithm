import heapq

N, M, R = map(int, input().split())
lst = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

answer = []

for i in range(1, N+1):
    q = []
    heapq.heappush(q, (0, i))
    visited = [float("inf")] * (N + 1)

    visited[i] = 0
    cnt = 0

    while q:
        cost, node = heapq.heappop(q)

        for next_node, next_cost in graph[node]:
            temp = next_cost + cost
            if temp < visited[next_node]:
                visited[next_node] = temp
                heapq.heappush(q, (temp, next_node))

    for j in range(1, N+1):
        if visited[j] <= M:
            cnt += lst[j-1]
    answer.append(cnt)

print(max(answer))