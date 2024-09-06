MAP = []
for _ in range(9):
    MAP.append(list(map(int, input())))

empty = []
for i in range(9):
    for j in range(9):
        if MAP[i][j] == 0:
            empty.append((i, j))

def is_valid(x, y, num):
    for i in range(9):
        if MAP[x][i] == num or MAP[i][y] == num:
            return False

    box_x, box_y = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if MAP[box_x + i][box_y + j] == num:
                return False

    return True

def solve_sudoku(cnt):
    if cnt == len(empty):
        for row in MAP:
            print(''.join(map(str, row)))
        exit(0)

    x, y = empty[cnt]

    for i in range(1, 10):
        if is_valid(x, y, i):
            MAP[x][y] = i
            solve_sudoku(cnt + 1)
            MAP[x][y] = 0

solve_sudoku(0)