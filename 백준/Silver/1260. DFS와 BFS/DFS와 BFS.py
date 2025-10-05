from collections import deque

N, M, V = map(int, input().split())

MAP = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    MAP[a][b] = 1
    MAP[b][a] = 1

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in range(1, N + 1):
        if MAP[v][i] == 1 and not visited_dfs[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited_bfs[v] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N + 1):
            if MAP[v][i] == 1 and not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True

dfs(V)
print()
bfs(V)
