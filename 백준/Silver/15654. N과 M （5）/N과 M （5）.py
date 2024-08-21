N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

comp = []
visited = [False] * N
def dfs(stack):
    if len(stack) == M:
        comp.append(stack[:])
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            stack.append(lst[i])
            dfs(stack)
            stack.pop()
            visited[i] = False

dfs([])

for i in comp:
    print(" ".join(map(str, i)))
