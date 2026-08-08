from collections import deque

for t in range(1, int(input())+1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N+1)
    answer = 0

    for i in range(1, N+1):
        if visited[i]:
            continue

        answer += 1

        q = deque()
        q.append(i)
        visited[i] = True

        while q:
            node = q.popleft()

            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)

    print(f"#{t} {answer}")