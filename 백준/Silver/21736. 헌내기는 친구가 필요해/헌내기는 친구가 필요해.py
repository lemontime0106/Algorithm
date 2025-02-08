from collections import deque

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
visited = [([False] * M) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

q = deque()

for i in range(N):
    for j in range(M):
        if MAP[i][j] == "I":
            q.append([i, j])

while q:
    x, y = q.popleft()

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and MAP[nx][ny] != "X":
            if MAP[nx][ny] == "P":
                answer += 1
            visited[nx][ny] = True
            q.append([nx, ny])

print(answer if answer != 0 else "TT")


