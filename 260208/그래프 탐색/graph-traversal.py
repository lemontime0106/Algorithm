N, M = map(int, input().split())
MAP = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    MAP[a].append(b)
    MAP[b].append(a)

visited = [False] * (N+1)
visited[1] = True

stack = [1]

def dfs():
    while stack:
        now = stack.pop()

        for nxt in MAP[now]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

dfs()

answer = 0

for i in visited[2:]:
    if i:
        answer += 1

print(answer)
