from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def bfs(x):
    q = deque()
    q.append(x)
    check = [0] * N

    while q:
        n = q.popleft()

        for i in range(N):
            if check[i] == 0 and graph[n][i] == 1:
                q.append(i)
                check[i] = 1
                visited[x][i] = 1

for i in range(0, N):
    bfs(i)

for i in visited:
    print(*i)