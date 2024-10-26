import sys
sys.setrecursionlimit(150000)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
cnt = 1

def dfs(start):
    global cnt

    visited[start] = cnt
    graph[start].sort()

    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(R)

for i in range(1, N+1):
    print(visited[i])