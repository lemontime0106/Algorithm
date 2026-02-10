from collections import deque

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

r, c = map(int, input().split())
r -= 1
c -= 1

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    start_value = MAP[x][y]
    lst = []

    while q:
        x, y = q.popleft()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and MAP[nx][ny] < start_value:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    lst.append((MAP[nx][ny], nx, ny))

    if not lst:
        return None

    lst.sort(key = lambda x: (-x[0], x[1], x[2]))
    return lst[0][1], lst[0][2]

for _ in range(K):
    answer = bfs(r, c)
    if answer is None:
        break

    r, c = answer

print(r+1, c+1)