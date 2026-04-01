n, m = map(int, input().split())
castle = [input().strip() for _ in range(n)]

empty_row = 0
for i in range(n):
    if 'X' not in castle[i]:
        empty_row += 1

empty_col = 0
for j in range(m):
    has_guard = False
    for i in range(n):
        if castle[i][j] == 'X':
            has_guard = True
            break
    if not has_guard:
        empty_col += 1

print(max(empty_row, empty_col))