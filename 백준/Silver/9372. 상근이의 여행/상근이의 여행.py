T = int(input())

def dfs(start, cnt):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            cnt = dfs(i, cnt + 1)
    return cnt

for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = dfs(1, 0)

    print(answer)