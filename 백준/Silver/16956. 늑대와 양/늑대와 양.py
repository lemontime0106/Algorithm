R, C = map(int, input().split())

MAP = [list(input()) for _ in range(R)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

flag = False

for i in range(R):
    for j in range(C):
        if MAP[i][j] == "W":
            for dx, dy in direct:
                nx, ny = i + dx, j + dy

                if 0 <= nx < R and 0 <= ny < C:
                    if MAP[nx][ny] == "S":
                        flag = True
                        break


if flag:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if MAP[i][j] == ".":
                MAP[i][j] = "D"

    for m in MAP:
        print("".join(m))