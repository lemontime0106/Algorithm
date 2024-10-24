from collections import deque

N = int(input())
MAP = [list(map(int, input())) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque()
visited = [[float("inf")] * N for _ in range(N)]

q.append((0, 0))
visited[0][0] = 0

while q:
    x, y = q.popleft()

    for d in direct:
        nx, ny = x + d[0], y + d[1]

        if 0 <= nx < N and 0 <= ny < N:
            if MAP[nx][ny] == 1 and visited[nx][ny] > visited[x][y]:
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx, ny))
            elif MAP[nx][ny] == 0 and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

print(visited[N-1][N-1])