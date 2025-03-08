MAP = [list(map(str, input().split())) for _ in range(5)]

answer = set()

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, number):
    if len(number) == 6:
        answer.add(number)
        return

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, number + MAP[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, MAP[i][j])

print(len(answer))