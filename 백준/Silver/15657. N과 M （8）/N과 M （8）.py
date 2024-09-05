N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

answer = []

def dfs(start, stack):
    if len(stack) == M:
        answer.append(stack[:])
        return

    for i in range(start, N):
        stack.append(lst[i])
        dfs(i, stack)
        stack.pop()

dfs(0, [])

for i in answer:
    print(*i)