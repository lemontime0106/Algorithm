from collections import deque

N = int(input())
MAP = [list(input()) for _ in range(N)]

answer = []
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

normal_visited = [[False] * N for _ in range(N)]
normal_cnt = 0
blind_visited = [[False] * N for _ in range(N)]
blind_cnt = 0

def normal(row, col):
    q = deque()
    q.append([row, col])
    normal_visited[row][col] = True

    color = MAP[row][col]

    while q:
        x, y = q.popleft()

        for d in direct:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and not normal_visited[nx][ny]:
                if color == MAP[nx][ny]:
                    normal_visited[nx][ny] = True
                    q.append([nx, ny])

def blind(row, col):
    q = deque()
    q.append([row, col])
    blind_visited[row][col] = True

    color = MAP[row][col]

    while q:
        x, y = q.popleft()

        for d in direct:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and not blind_visited[nx][ny]:
                if (color == "R" or color == "G") and (MAP[nx][ny] == "R" or MAP[nx][ny] == "G"):
                    blind_visited[nx][ny] = True
                    q.append([nx, ny])
                elif color == MAP[nx][ny]:
                    blind_visited[nx][ny] = True
                    q.append([nx, ny])


for i in range(N):
    for j in range(N):
        if not normal_visited[i][j]:
            normal(i, j)
            normal_cnt += 1

        if not blind_visited[i][j]:
            blind(i, j)
            blind_cnt += 1

print(normal_cnt, blind_cnt)