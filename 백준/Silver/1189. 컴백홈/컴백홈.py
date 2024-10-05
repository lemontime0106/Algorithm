R, C, K = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

def dfs(x, y, dist):
    global answer

    if dist == K and y == C-1 and x == 0:
        answer += 1

    else:
        for d in direct:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < R and 0 <= ny < C and MAP[nx][ny] == ".":
                MAP[nx][ny] = "T"
                dfs(nx, ny, dist+1)
                MAP[nx][ny] = "."

MAP[R-1][0] = "T"
dfs(R-1, 0, 1)
print(answer)