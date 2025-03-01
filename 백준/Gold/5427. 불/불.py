from collections import deque

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    cnt = 0
    while q:
        cnt += 1

        while fire and fire[0][2] < cnt:
            x, y, time = fire.popleft()

            for dx, dy in direct:
                nx, ny = x + dx, y + dy

                if 0 <= nx < M and 0 <= ny < N:
                    if MAP[nx][ny] == "." or MAP[nx][ny] == "@":
                        MAP[nx][ny] = "*"
                        fire.append((nx, ny, time + 1))

        while q and q[0][2] < cnt:
            x, y, time = q.popleft()
            for dx, dy in direct:
                nx, ny = x + dx, y + dy

                if 0 <= nx < M and 0 <= ny < N:
                    if MAP[nx][ny] == "." and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, time + 1))

                else:
                    return cnt

    return "IMPOSSIBLE"



for _ in range(int(input())):
    N, M = map(int, input().split())
    MAP = [list(input()) for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    q = deque()
    fire = deque()
    for i in range(M):
        for j in range(N):
            if MAP[i][j] == "@":
                visited[i][j] = True
                q.append((i, j, 0))

            if MAP[i][j] == "*":
                fire.append((i, j, 0))

    print(bfs())