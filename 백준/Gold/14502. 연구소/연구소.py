from collections import deque
import copy

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = 0

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def makewall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                makewall(cnt + 1)
                MAP[i][j] = 0

def bfs():
    global answer
    wall = copy.deepcopy(MAP)
    q = deque()

    for i in range(N):
        for j in range(M):
            if wall[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for d in direct:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < N and 0 <= ny < M and wall[nx][ny] == 0:
                wall[nx][ny] = 2
                q.append((nx, ny))

    safe = 0
    for i in wall:
        safe += i.count(0)
    answer = max(answer, safe)

makewall(0)

print(answer)