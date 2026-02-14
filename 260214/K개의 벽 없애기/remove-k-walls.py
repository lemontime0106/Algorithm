from collections import deque

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

visited = [[[False] * (K+1) for _ in range(N)] for _ in range(N)]

q = deque()
q.append((r1, c1, 0, 0))
visited[r1][c1][0] = True

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    x, y, broken, time = q.popleft()

    if x == r2 and y == c2:
        print(time)
        exit(0)

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if MAP[nx][ny] == 0 and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = True
                q.append((nx, ny, broken, time + 1))
            
            if MAP[nx][ny] == 1 and broken < K and not visited[nx][ny][broken+1]:
                visited[nx][ny][broken+1] = True
                q.append((nx, ny, broken+1, time+1))

print(-1) 