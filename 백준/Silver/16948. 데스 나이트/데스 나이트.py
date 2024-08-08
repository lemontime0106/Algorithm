from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

direct = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
visited = [[False] * N for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        x, y, cnt = q.popleft()
        if x == r2 and y == c2:
            print(cnt)
            return

        for d in direct:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True

    print(-1)


bfs(r1, c1)
