from collections import deque

N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True

    total = MAP[x][y]
    union = [(x, y)]

    while q:
        x, y = q.popleft()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(MAP[nx][ny] - MAP[x][y]) <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total += MAP[nx][ny]

    return union, total

answer = 0
while True:
    flag = False
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, total = bfs(i, j, visited)

                if len(union) > 1:
                    flag = True
                    new_value = total // len(union)
                    for nx, ny in union:
                        MAP[nx][ny] = new_value

    if not flag:
        break

    answer += 1

print(answer)
