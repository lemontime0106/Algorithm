from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)

bfs(1)
answer = max(visited)
print(visited.index(answer), answer-1, visited.count(answer))