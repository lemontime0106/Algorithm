import heapq

for _ in range(int(input())):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(D):
        a, b, c = map(int, input().split())
        graph[b].append([a, c])

    visited = [float("inf")] * (N+1)
    q = []
    heapq.heappush(q, [0, C])
    visited[C] = 0

    while q:
        time, node = heapq.heappop(q)
        for next_node, next_time in graph[node]:
            cost = next_time + time
            if visited[next_node] > cost:
                visited[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    cnt, answer = 0, 0

    for i in visited:
        if i != float("inf"):
            cnt += 1
            answer = max(answer, i)

    print(cnt, answer)