from collections import deque

for _ in range(10):
    t = int(input())
    MAP = [list(map(int, input())) for _ in range(16)]

    start_x, start_y = 0, 0

    for y in range(16):
        for x in range(16):
            if MAP[y][x] == 2:
                start_x = x
                start_y = y

    q = deque()
    q.append((start_y, start_x))

    visited = [[False] * 16 for _ in range(16)]
    visited[start_y][start_x] = True

    answer = 0

    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        y, x = q.popleft()

        if MAP[y][x] == 3:
            answer = 1
            break

        for dx, dy in direct:
            ny, nx = y + dy, x + dx

            if 0 <= ny < 16 and 0 <= nx < 16:
                if MAP[ny][nx] != 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

    print(f"#{t} {answer}")