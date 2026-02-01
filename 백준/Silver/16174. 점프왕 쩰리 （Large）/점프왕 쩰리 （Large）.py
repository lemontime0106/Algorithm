N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    if visited[x][y]:
        return False

    if MAP[x][y] == -1:
        return True

    visited[x][y] = True
    jump = MAP[x][y]

    if jump == 0:
        return False

    return dfs(x + jump, y) or dfs(x, y + jump)

if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")