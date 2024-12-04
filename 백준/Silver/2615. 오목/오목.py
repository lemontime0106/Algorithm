MAP = [list(map(int, input().split())) for _ in range(19)]

direct = [(1, 0), (0, 1), (1, 1), (-1, 1)]

color = 0
point = [0, 0]

for i in range(19):
    for j in range(19):
        if MAP[i][j]:
            for dx, dy in direct:
                nx, ny = i + dx, j + dy
                cnt = 1

                while 0 <= nx < 19 and 0 <= ny < 19 and MAP[i][j] == MAP[nx][ny]:
                    cnt += 1
                    nx += dx
                    ny += dy

                if cnt == 5:
                    prev_x, prev_y = i - dx, j - dy
                    if 0 <= prev_x < 19 and 0 <= prev_y < 19 and MAP[prev_x][prev_y] == MAP[i][j]:
                        continue

                    next_x, next_y = i + 5 * dx, j + 5 * dy
                    if 0 <= next_x < 19 and 0 <= next_y < 19 and MAP[next_x][next_y] == MAP[i][j]:
                        continue

                    color = MAP[i][j]
                    point = [i + 1, j + 1]  # 1-based index
                    break
            if color:
                break
    if color:
        break

if not color:
    print(0)
else:
    print(color)
    print(*point)
