from collections import deque

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if MAP[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())

    MAP = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())

        MAP[x][y] = 1

    answer = 0

    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if MAP[i][j] and not visited[i][j]:
                bfs(i, j)
                answer += 1

    print(answer)