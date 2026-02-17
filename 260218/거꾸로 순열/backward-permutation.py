N = int(input())

visited = [False] * (N+1)
lst = []

def dfs():
    if len(lst) == N:
        print(*lst)
        return

    for i in range(N, 0, -1):
        if not visited[i]:
            visited[i] = True
            lst.append(i)
            dfs()
            lst.pop()
            visited[i] = False

dfs()