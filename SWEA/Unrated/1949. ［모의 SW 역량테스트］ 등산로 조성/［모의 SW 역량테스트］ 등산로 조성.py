direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_maxlen(x, y, cnt, lst, v):
    global ans
    ans = max(ans, cnt)

    for d in range(4):
        nx = x + direct[d][0]
        ny = y + direct[d][1]
        if 0 <= nx < N and 0 <= ny < N and not v[nx][ny]:
            if lst[x][y] > lst[nx][ny]:
                v[nx][ny] = True
                find_maxlen(nx, ny, cnt+1, lst, v)
                v[nx][ny] = False


for T in range(int(input())):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    top = 0
    start_list = []
    for i in range(N):
        for j in range(N):
            if top <= MAP[i][j]:
                top = MAP[i][j]

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == top:
                start_list.append((i, j))

    for start in start_list:
        for i in range(N):
            for j in range(N):
                if (start[0], start[1]) == (i, j):
                    # print(1)
                    continue
                for k in range(K+1):
                    lst = [row[:] for row in MAP]
                    lst[i][j] -= k
                    if lst[i][j] < 0:
                        lst[i][j] = 0
                    #
                    # for ii in lst:
                    #     for jj in ii:
                    #         print(jj, end=' ')
                    #     print()
                    # print()

                    visited = [[False] * N for _ in range(N)]
                    visited[start[0]][start[1]] = True
                    find_maxlen(start[0], start[1], 1, lst, visited)

    print(f'#{T+1}', ans)