N = int(input())
M = int(input())

MAP = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    MAP[a].append(b)
    MAP[b].append(a)

visited = [False] * N

def dfs(cur):
    visited[cur] = True

    for nxt in MAP[cur]:
        if not visited[nxt]:
            dfs(nxt)

dfs(0)

answer = 0

for i in visited:
    if i:
        answer += 1

print(answer-1)