import sys
sys.setrecursionlimit(10 ** 5)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)
cnt = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    global cnt
    visited[x] = True

    answer[x] = cnt
    graph[x].sort(reverse=True)

    for i in graph[x]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(R)

for i in answer[1:]:
    print(i)