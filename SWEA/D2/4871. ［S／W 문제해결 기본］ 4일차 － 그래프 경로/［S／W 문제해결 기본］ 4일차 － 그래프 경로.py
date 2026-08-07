from collections import deque

for t in range(1, int(input())+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())

        graph[a].append(b)

    start, end = map(int, input().split())

    visited = [False] * (V+1)
    q = deque()
    q.append(start)
    visited[start] = True

    answer = 0

    while q:
        node = q.popleft()

        if node == end:
            answer = 1
            break

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    print(f"#{t} {answer}")
