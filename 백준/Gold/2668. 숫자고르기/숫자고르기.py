N = int(input())
lst = [0] + [int(input()) for _ in range(N)]
answer = []

def dfs(v, i):
    visited[v] = True
    node = lst[v]

    if not visited[node]:
        dfs(node, i)
    elif visited[node] and node == i:
        answer.append(node)

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)

print(len(answer))
for i in answer:
    print(i)