from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque()
q.append((0, 0))
visited[0][0] = 0

while q:
    x, y = q.popleft()

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == -1 and MAP[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[N-1][M-1])