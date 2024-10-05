N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

answer = float("inf")
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * N for _ in range(N)]

def flower_cost(x, y):
    cost = MAP[x][y]
    for d in direct:
        nx, ny = x + d[0], y + d[1]
        cost += MAP[nx][ny]
    return cost

def can_flower(x, y):
    if visited[x][y]:
        return False

    for d in direct:
        nx, ny = x + d[0], y + d[1]
        if visited[nx][ny]:
            return False
    return True

def place_flower(x, y, flag):
    visited[x][y] = flag
    for d in direct:
        nx, ny = x + d[0], y + d[1]
        visited[nx][ny] = flag

def backtracking(cnt, cost):
    global answer

    if cnt == 3:
        answer = min(answer, cost)
        return

    for i in range(1, N-1):
        for j in range(1, N-1):
            if can_flower(i, j):
                value = flower_cost(i, j)
                place_flower(i, j, True)
                backtracking(cnt + 1, cost + value)
                place_flower(i, j, False)

backtracking(0, 0)
print(answer)
