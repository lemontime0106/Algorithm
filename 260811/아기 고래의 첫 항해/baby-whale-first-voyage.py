from collections import deque

N, r, c, d = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

direct = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}

priority = {
    1: [1, 3, 4, 2],
    2: [2, 4, 3, 1],
    3: [3, 2, 1, 4],
    4: [4, 1, 2, 3]
}

bfs_order = [3, 2, 4, 1]

r -= 1
c -= 1

visited = [[False] * N for _ in range(N)]
visited[r][c] = True

answer = [(r, c)]

total_sea = 0

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 0:
            total_sea += 1

visited_count = 1

while visited_count < total_sea:
    while True:
        moved = False

        for nd in priority[d]:
            dx, dy = direct[nd]

            nx = r + dx
            ny = c + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if MAP[nx][ny] == 1:
                continue

            if visited[nx][ny]:
                continue

            r, c, d = nx, ny, nd

            visited[r][c] = True
            visited_count += 1
            
            answer.append((r, c))

            moved = True
            break
        
        if not moved:
            break
    
    if visited_count == total_sea:
        break

    
    dist = [[-1] * N for _ in range(N)]
    parent = [[None] * N for _ in range(N)]

    q = deque()

    q.append((r, c))
    dist[r][c] = 0

    while q:
        x, y = q.popleft()

        for nd in bfs_order:
            dx, dy = direct[nd]

            nx, ny = x + dx, y + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if MAP[nx][ny] == 1:
                continue

            if dist[nx][ny] != -1:
                continue

            dist[nx][ny] = dist[x][y] + 1
            parent[nx][ny] = (x, y)

            q.append((nx, ny))
    
    target = None

    for x in range(N):
        for y in range(N):
            if MAP[x][y] == 1:
                continue
            
            if visited[x][y]:
                continue

            if dist[x][y] == -1:
                continue

            candidate = (dist[x][y], x, y)

            if target is None or candidate < target:
                target = candidate
    
    if target is None:
        break

    _, tx, ty = target

    path = []

    x, y = tx, ty

    while (x, y) != (r, c):
        path.append((x, y))
        x, y = parent[x][y]

    path.reverse()

    px, py = r, c

    for x, y in path:
        if x == px - 1 and y == py:
            d = 1

        elif x == px + 1 and y == py:
            d = 2
        
        elif x == px and y == py - 1:
            d = 3

        elif x == px and y == py + 1:
            d = 4

        px, py = x, y

    r, c = tx, ty

    visited[r][c] = True
    visited_count += 1

    answer.append((r, c))

for x, y in answer:
    print(x + 1, y + 1)