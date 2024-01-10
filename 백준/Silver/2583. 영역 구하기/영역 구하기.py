import sys
sys.setrecursionlimit(10**5)

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, v, c):
    if MAP[x][y] == 0 and v[x][y] == 0:
        c += 1
        v[x][y] = 1

        for d in direct:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                c = dfs(nx, ny, v, c)  # 재귀 호출 시 c 값을 업데이트

    return c

M, N, K = map(int, input().split())

MAP = [[0] * M for _ in range(N)]

for _ in range(K):
    a, b, c, d = map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            MAP[i][j] = 1

visited = [[0] * M for _ in range(N)]
lst = []

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            cnt = dfs(i, j, visited, 0)
            if cnt != 0:
                lst.append(cnt)

lst.sort()
print(len(lst))
print(*lst)