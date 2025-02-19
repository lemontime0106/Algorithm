from collections import deque

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

direct = [(1, 0), (0, 1)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        cnt = MAP[x][y]

        if MAP[x][y] == -1:
            return True

        for dx, dy in direct:
            nx, ny = x + dx * cnt, y + dy * cnt

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])

    return False

if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")
