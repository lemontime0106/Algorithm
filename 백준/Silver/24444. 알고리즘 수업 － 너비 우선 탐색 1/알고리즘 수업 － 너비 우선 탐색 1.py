from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visited = [0] * (N+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    cnt = 2

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = cnt
                cnt += 1
bfs(R)

for i in visited[1:]:
    print(i)

