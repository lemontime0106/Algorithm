from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (N+1)
visited[X] = 0

def bfs(x):
    q = deque([x])

    while q:
        node = q.popleft()

        for i in graph[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + 1
                q.append(i)


bfs(X)

answer = [i for i in range(1, N+1) if visited[i] == K]

if answer:
    for city in answer:
        print(city)
else:
    print(-1)