from collections import deque

N, M = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count

# 각 노드에 대해 BFS 수행하여 해킹 가능한 노드 수 계산
hacking_counts = []
max_hacks = 0

for i in range(1, N + 1):
    hacks = bfs(i)
    hacking_counts.append((i, hacks))
    if hacks > max_hacks:
        max_hacks = hacks

# 해킹 가능한 노드 수가 가장 많은 노드를 출력
for node, count in hacking_counts:
    if count == max_hacks:
        print(node, end=' ')