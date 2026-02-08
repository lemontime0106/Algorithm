N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
direct = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x, y):
    cnt = 1
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and MAP[nx][ny] == 1:
                visited[nx][ny] = True
                cnt += dfs(nx, ny)
    return cnt

answer = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            answer.append(dfs(i, j))

print(len(answer))
answer.sort()
for x in answer:
    print(x)
