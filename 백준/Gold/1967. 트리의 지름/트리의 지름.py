import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())


graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(node, distance):
    global max_distance, far_node

    visited[node] = True

    if distance > max_distance:
        max_distance = distance
        far_node = node

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, distance + weight)

# 1번 노드에서 가장 먼 노드 찾기
visited = [False] * (N+1)
max_distance = 0
far_node = 0
dfs(1, 0)

# 찾은 가장 먼 노드에서 다시 DFS 돌려서 트리의 지름 구하기
visited = [False] * (N+1)
max_distance = 0
dfs(far_node, 0)

print(max_distance)
# 최적해 방식