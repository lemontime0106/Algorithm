R, C = map(int, input().split())

MAP = [list(input().strip()) for _ in range(R)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

lst = set()
answer = 0

def dfs(x, y, cnt):
    global answer

    if answer < cnt:
        answer = cnt

    if cnt == 26:
        print("26")
        exit(0)

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < R and 0 <= ny < C and MAP[nx][ny] not in lst:
            lst.add(MAP[nx][ny])
            dfs(nx, ny, cnt + 1)
            lst.remove(MAP[nx][ny])

lst.add(MAP[0][0])
dfs(0, 0, 1)
print(answer)