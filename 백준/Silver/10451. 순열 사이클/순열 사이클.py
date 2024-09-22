from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    MAP = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        MAP[i].append(lst[i-1])

    visited = [False] * (N+1)
    answer = 0
    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = True

        while q:
            v = q.popleft()
            nv = MAP[v][0]
            if not visited[nv]:
                q.append(nv)
                visited[nv] = True

    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            answer += 1

    print(answer)


