from collections import deque

N, K, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

start_spot = [list(map(int, input().split())) for _ in range(K)]
rock = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            rock.append((i, j))

answer = 0

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    visited = [[False]*N for _ in range(N)]
    q = deque()
    cnt = 0

    for x, y in start_spot:
        x -= 1
        y -= 1
        if MAP[x][y] == 0 and not visited[x][y]:
            visited[x][y] = True
            q.append((x, y))
            cnt += 1

    while q:
        x, y = q.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and MAP[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1

    return cnt

def backtracking(idx, cnt):
    global answer
    
    if cnt == M:
        answer = max(answer, bfs())
        return

    if idx == len(rock):
        return
    
    if len(rock) - idx < M - cnt:
        return
    
    x, y = rock[idx]

    MAP[x][y] = 0
    backtracking(idx + 1, cnt + 1)
    MAP[x][y] = 1

    backtracking(idx + 1, cnt)

backtracking(0, 0)

print(answer)