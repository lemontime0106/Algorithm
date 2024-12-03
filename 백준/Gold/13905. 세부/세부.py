from collections import deque

N, M = map(int, input().split())
S, E = map(int, input().split())

answer = 0
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

left, right = 1, 10 ** 6

while left <= right:
    mid = (left + right) // 2
    flag = False

    visited = [False] * (N+1)
    q = deque()
    q.append(S)
    visited[S] = True
    while q:
        now = q.popleft()
        if now == E:
            flag = True
            break

        for node, weight in graph[now]:
            if not visited[node] and weight >= mid:
                q.append(node)
                visited[node] = True

    if flag:
        answer = mid
        left = mid + 1
    else:
        right = mid -1

print(answer)
