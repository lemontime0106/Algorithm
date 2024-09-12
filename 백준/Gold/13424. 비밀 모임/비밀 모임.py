import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, node = heapq.heappop(q)
        if cost > distance[node]:
            continue

        for next_node, next_cost in graph[node]:
            total = cost + next_cost
            if total < distance[next_node]:
                distance[next_node] = total
                heapq.heappush(q, (total, next_node))

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    answer = [0] * (N+1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    K = int(input())
    friend = list(map(int, input().split()))

    for i in friend:
        distance = [float("inf")] * (N+1)
        dijkstra(i)
        for j in range(1, N+1):
            answer[j] += distance[j]

    ans = 0
    temp = float("inf")
    for i in range(1, N+1):
        if temp > answer[i]:
            temp = answer[i]
            ans = i

    print(ans)