from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, v):
    global ans
    q = deque()
    q.append((x, y))
    v[x][y] = 2
    ans += 1
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + direct[k][0]
            ny = y + direct[k][1]
            if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 1:
                v[nx][ny] = 2
                q.append((nx, ny))


direct = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

while True:
    M, N = map(int, input().split())
    if N == 0 and M == 0:
        break
    ans = 0
    MAP = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                bfs(i, j, MAP)

    print(ans)