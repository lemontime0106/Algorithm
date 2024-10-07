N, M = map(int, input().split())
R, C, D = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
visited[R][C] = True
cnt = 1

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    flag = False
    for _ in range(4):
        D = (D + 3) % 4
        nr, nc = R + direct[D][0], C + direct[D][1]

        if 0 <= nr < N and 0 <= nc < M and not MAP[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = True
            cnt += 1
            R, C = nr, nc
            flag = True
            break

    if not flag:
        back_r, back_c = R - direct[D][0], C - direct[D][1]
        if 0 <= back_r < N and 0 <= back_c < M and not MAP[back_r][back_c]:
            R, C = back_r, back_c
        else:
            print(cnt)
            break
