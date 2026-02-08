N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

direct = [(1, 0), (0, 1)]

stack = [(0, 0)]
visited[0][0] = True
answer = 0

while stack:
    x, y = stack.pop()

    if x == N-1 and y == M-1:
        answer = 1
        break

    for dx, dy in direct:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and MAP[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))
                visited[nx][ny] = False

print(answer)