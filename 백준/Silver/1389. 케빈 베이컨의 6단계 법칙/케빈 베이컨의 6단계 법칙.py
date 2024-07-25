from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = visited[now] + 1
                q.append(i)

answer = []

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    bfs(i)
    answer.append(sum(visited))

print(answer.index(min(answer)) + 1)