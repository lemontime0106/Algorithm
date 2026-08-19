# 1219. [S/W 문제해결 기본] 4일차 - 길찾기

from collections import deque

for _ in range(10):
    T, N = map(int, input().split())
    lst = list(map(int, input().split()))

    graph = [[] for _ in range(100)]

    for i in range(0, N*2, 2):
        start, end = lst[i], lst[i+1]

        graph[start].append(end)

    q = deque([0])
    visited = [False] * 100
    visited[0] = True

    answer = 0

    while q:
        node = q.popleft()

        if node == 99:
            answer = 1
            break

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    print(f"#{T} {answer}")