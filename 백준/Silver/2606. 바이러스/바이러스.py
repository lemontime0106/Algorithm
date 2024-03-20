N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)

dfs(1, visited)

ans = 0
for i in visited:
    if i:
        ans += 1

print(ans - 1)