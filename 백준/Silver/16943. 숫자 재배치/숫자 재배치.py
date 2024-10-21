def dfs(start, cnt, length, stack):
    if cnt == length:
        if stack[0] == "0":
            return

        lst.append(int("".join(stack[:])))
        return

    for i in range(len(A)):
        if not visited[i]:
            visited[i] = True
            stack.append(A[i])
            dfs(start+1, cnt+1, length, stack)
            stack.pop()
            visited[i] = False


A, B = map(int, input().split())

A = list(str(A))

visited = [False] * len(A)

lst = []

dfs(0, 0, len(A), [])

lst.sort()
# print(lst)
ans = -1

for i in range(len(lst)):
    if lst[i] > B:
        break
    ans = lst[i]

print(ans)

