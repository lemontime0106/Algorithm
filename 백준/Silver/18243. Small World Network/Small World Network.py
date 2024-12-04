from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = []

def bfs(start):
    q = deque()
    visited = [-1] * (N+1)
    q.append(start)
    visited[start] = 0

    while q:
        now = q.popleft()

        for node in graph[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                q.append(node)

    if visited[1:].count(-1):
        return -1

    return max(visited)

for i in range(1, N+1):
    cnt = bfs(i)
    if cnt == -1:
        print("Big World!")
        exit()
    else:
        answer.append(cnt)

if max(answer) > 6:
    print("Big World!")
else:
    print("Small World!")
