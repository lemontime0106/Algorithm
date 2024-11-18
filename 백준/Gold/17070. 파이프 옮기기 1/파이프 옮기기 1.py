from collections import deque
import sys

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0

def dfs(x, y, state):
    global answer
    if x == N - 1 and y == N - 1:
        answer += 1
        return

        # 가로 방향
    if state == 0:
        if y == N - 1:
            return

        if y + 1 < N and not MAP[x][y + 1]:
            dfs(x, y + 1, 0)

        if x + 1 < N and y + 1 < N and not MAP[x][y + 1] and not MAP[x + 1][y] and not MAP[x + 1][y + 1]:
            dfs(x + 1, y + 1, 2)

    # 세로 방향
    elif state == 1:
        if x == N - 1:  # 이동불가
            return

        if x + 1 < N and not MAP[x + 1][y]:
            dfs(x + 1, y, 1)

        if x + 1 < N and y + 1 < N and not MAP[x][y + 1] and not MAP[x + 1][y] and not MAP[x + 1][y + 1]:
            dfs(x + 1, y + 1, 2)

    # 대각선 방향
    elif state == 2:
        if y + 1 < N and not MAP[x][y + 1]:
            dfs(x, y + 1, 0)

        if x + 1 < N and not MAP[x + 1][y]:
            dfs(x + 1, y, 1)

        if x + 1 < N and y + 1 < N and not MAP[x][y + 1] and not MAP[x + 1][y] and not MAP[x + 1][y + 1]:
            dfs(x + 1, y + 1, 2)

dfs(0, 1, 0)
print(answer)