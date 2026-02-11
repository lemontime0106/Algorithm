from collections import deque

N, K, U, D = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    result = {(x, y)}

    while q:
        x, y = q.popleft()

        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    diff = abs(MAP[x][y] - MAP[nx][ny])

                    if U <= diff <= D:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        result.add((nx, ny))

    return result

city = [(i, j) for i in range(N) for j in range(N)]
answer = 0
selected = []

def dfs(idx, cnt):
    global answer

    if cnt == K:
        visited_all = set()
        for x, y in selected:
            visited_all |= bfs(x, y)
        answer = max(answer, len(visited_all))
    
    if idx == len(city):
        return
    
    if len(city) - idx < K - cnt:
        return

    selected.append(city[idx])
    dfs(idx+1, cnt+1)
    selected.pop()

    dfs(idx + 1, cnt)

dfs(0, 0)
print(answer)