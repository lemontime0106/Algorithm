import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

visited = [0] * (N + 1)
order = 1

def bfs(start):
    global order
    q = deque([start])
    visited[start] = order

    while q:
        u = q.popleft()
        for v in graph[u]:
            if visited[v] == 0:
                order += 1
                visited[v] = order
                q.append(v)

bfs(R)

print('\n'.join(map(str, visited[1:])))