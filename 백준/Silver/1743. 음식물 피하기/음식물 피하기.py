from collections import deque

N, M, K = map(int, input().split())
MAP = [[0] * M for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    MAP[a-1][b-1] = 1

direct = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited = [[False] * M for _ in range(N)]

answer = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()

        for d in direct:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if MAP[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))

    return cnt

for i in range(N):
    for j in range(M):
        if not visited[i][j] and MAP[i][j] == 1:
            answer.append(bfs(i, j))

print(max(answer))
