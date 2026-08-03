from collections import deque

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(10):
    t = int(input())
    MAP = [list(map(int, input())) for _ in range(100)]
    answer = 0

    start_x, start_y = 0, 0

    for x in range(100):
        for y in range(100):
            if MAP[x][y] == 2:
                start_x, start_y = x, y

    q = deque()
    q.append((start_x, start_y))

    visited = [[False] * 100 for _ in range(100)]
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        if MAP[x][y] == 3:
            answer = 1
            break

        for dx, dy in direct:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 100 and 0 <= ny < 100:
                if MAP[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    print(f"#{t} {answer}")