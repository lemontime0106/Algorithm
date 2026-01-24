from collections import deque

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def bfs(x):
    q = deque()
    q.append(x)
    lst = [0] * N

    while q:
        y = q.popleft()

        for i in range(N):
            if lst[i] == 0 and MAP[y][i] == 1:
                q.append(i)
                lst[i] = 1
                visited[x][i] = 1

for i in range(N):
    bfs(i)

for i in visited:
    print(*i)