from collections import deque

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque()
q.append((x1-1, y1-1))
visited[x1-1][y1-1] = 0

while q:
    x, y = q.popleft()

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
            if MAP[nx][ny] == "1" or MAP[nx][ny] == "#":
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            elif MAP[nx][ny] == "0":
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx, ny))

print(visited[x2-1][y2-1])