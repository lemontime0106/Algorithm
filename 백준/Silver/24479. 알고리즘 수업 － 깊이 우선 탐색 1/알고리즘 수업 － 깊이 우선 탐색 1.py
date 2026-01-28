import sys
sys.setrecursionlimit(150000)

N, M, R = map(int, input().split())

MAP = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    MAP[a].append(b)
    MAP[b].append(a)

for i in range(1, N + 1):
    MAP[i].sort()

visited = [0] * (N + 1)
cnt = 1

def dfs(cur):
    global cnt
    visited[cur] = cnt
    cnt += 1

    for nxt in MAP[cur]:
        if visited[nxt] == 0:
            dfs(nxt)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
