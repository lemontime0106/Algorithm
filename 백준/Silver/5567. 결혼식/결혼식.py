from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def bfs(x):
    q = deque([x])
    visited[x] = 1

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[x] + 1

bfs(1)
answer = 0
for i in range(2, N+1):
    if 0 < visited[i] <= 3:
        answer += 1

print(answer)