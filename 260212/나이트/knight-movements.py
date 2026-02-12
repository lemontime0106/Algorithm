from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

visited = [[-1] * N for _ in range(N)]

direct = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

q = deque()
q.append((r1-1, c1-1))
visited[r1-1][c1-1] = 0

while q:
    x, y = q.popleft()

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[r2-1][c2-1])