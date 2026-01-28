N, M = map(int, input().split())

MAP = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    MAP[b].append(a)

def dfs(start):
    visited = [False] * N
    stack = [start]
    visited[start] = True
    cnt = 1

    while stack:
        cur = stack.pop()
        for nxt in MAP[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                stack.append(nxt)
    return cnt

max_value = 0
result = []

for i in range(N):
    value = dfs(i)
    if value > max_value:
        max_value = value
        result = [i + 1]
    elif value == max_value:
        result.append(i + 1)

print(*result)
