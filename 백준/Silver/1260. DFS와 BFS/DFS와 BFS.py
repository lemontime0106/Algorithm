from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# print(graph)

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs_list = []
bfs_list = []

def dfs(start):
    visited_dfs[start] = True
    dfs_list.append(start)
    for i in graph[start]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited_bfs[start] = True
    while q:
        v = q.popleft()
        bfs_list.append(v)
        for i in graph[v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True

dfs(V)
bfs(V)
print(*dfs_list, end=' ')
print()
print(*bfs_list, end=' ')