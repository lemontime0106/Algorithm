N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [False] * N
answer = set()

def dfs(stack):
    if len(stack) == M:
        answer.add(tuple(stack[:]))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            stack.append(lst[i])
            dfs(stack)
            stack.pop()
            visited[i] = False

dfs([])

for seq in sorted(answer):
    print(*seq)