def dfs(start, stack):
    if len(stack) == M:
        answer.add(tuple(stack))
        return

    for i in range(start, N):
        stack.append(lst[i])
        dfs(i, stack)
        stack.pop()

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))

answer = set()

dfs(0, [])

for a in sorted(answer):
    print(*a)
