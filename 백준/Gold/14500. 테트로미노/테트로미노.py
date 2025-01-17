N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 0

def dfs(x, y, temp, cnt): # 나머지
    global answer

    if cnt == 4:
        answer = max(answer, temp)
        return

    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, temp + MAP[nx][ny], cnt + 1)
            visited[nx][ny] = False

def dfs2(x, y): # T미노
    global answer

    temp = MAP[x][y]
    arr = []

    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            arr.append(MAP[nx][ny])

    length = len(arr)
    if length == 4:
        arr.sort()
        arr.pop(0)
        answer = max(answer, sum(arr) + MAP[x][y])
    elif length == 3:
        answer = max(answer, sum(arr) + MAP[x][y])
    return

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, MAP[i][j], 1)
        dfs2(i, j)
        visited[i][j] = False

print(answer)