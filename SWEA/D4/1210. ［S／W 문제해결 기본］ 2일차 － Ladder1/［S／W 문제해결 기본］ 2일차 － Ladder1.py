direct = [(0, -1), (0, 1), (1, 0)]

for _ in range(10):
    T = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]

    answer = 0

    for start_y in range(100):

        if MAP[0][start_y] != 1:
            continue

        x, y = 0, start_y

        visited = [[False] * 100 for _ in range(100)]
        visited[x][y] = True

        while x < 100:

            if MAP[x][y] == 2:
                answer = start_y
                break

            if y - 1 >= 0 and MAP[x][y - 1] == 1 and not visited[x][y - 1]:
                y -= 1
                visited[x][y] = True

            elif y + 1 < 100 and MAP[x][y + 1] == 1 and not visited[x][y + 1]:
                y += 1
                visited[x][y] = True

            elif x + 1 < 100 and MAP[x + 1][y] != 0:
                x += 1
                visited[x][y] = True

            else:
                break

        if MAP[x][y] == 2:
            break

    print(f"#{T} {answer}")