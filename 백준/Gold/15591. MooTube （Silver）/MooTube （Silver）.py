from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b, usado = map(int, input().split())
    graph[a].append((b, usado))
    graph[b].append((a, usado))

for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N+1)
    visited[v] = True
    answer = 0

    q = deque([(v, float("inf"))])

    while q:
        v, usado = q.popleft()
        for next_v, next_usado in graph[v]:
            next_usado = min(next_usado, usado)
            if not visited[next_v] and next_usado >= k:
                answer += 1
                visited[next_v] = True
                q.append((next_v, next_usado))

    print(answer)