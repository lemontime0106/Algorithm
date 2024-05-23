from collections import deque

N, M, T = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]

q = deque([(0, 0, 0)])
visited[0][0][0] = 0
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    x, y, sword = q.popleft()
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if sword == 0:
                if visited[nx][ny][0] == -1:
                    if MAP[nx][ny] == 0:
                        visited[nx][ny][0] = visited[x][y][0] + 1
                        q.append((nx, ny, 0))
                    elif MAP[nx][ny] == 2:
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        q.append((nx, ny, 1))
            else:
                if visited[nx][ny][1] == -1:
                    visited[nx][ny][1] = visited[x][y][1] + 1
                    q.append((nx, ny, 1))

result_1 = visited[N-1][M-1][0]
result_2 = visited[N-1][M-1][1]

if result_1 == -1 and result_2 == -1:
    print("Fail")
else:
    result = float('inf')
    if result_1 != -1:
        result = min(result, result_1)
    if result_2 != -1:
        result = min(result, result_2)

    if result > T:
        print("Fail")
    else:
        print(result)