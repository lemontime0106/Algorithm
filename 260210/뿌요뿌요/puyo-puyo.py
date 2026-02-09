N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, target):
    global cnt

    stack = [(x, y)]
    MAP[x][y] = 0

    while stack:
        x, y = stack.pop()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if MAP[nx][ny] == target:
                    MAP[nx][ny] = 0
                    cnt += 1
                    stack.append((nx, ny))


boom_cnt = 0
max_block = 0

for i in range(N):
    for j in range(N):
        if MAP[i][j] != 0:
            cnt = 1
            target = MAP[i][j]
            dfs(i, j, target)

            max_block = max(max_block, cnt)
            if cnt >= 4:
                boom_cnt += 1

print(boom_cnt, max_block)
