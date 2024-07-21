from collections import deque

N = int(input()) # 맵 크기
K = int(input()) # 사과 갯수
MAP = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    MAP[a-1][b-1] = 1

L = int(input()) # 이동 횟수
move = []
for _ in range(L):
    temp = list(input().split())
    temp[0] = int(temp[0])
    move.append(temp)

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q = deque()
q.append((0, 0))

h, hx, hy = 0, 0, 0
time, i = 0, 0

while True:
    hx, hy = hx + direct[h][0], hy + direct[h][1]
    time += 1
    if hx < 0 or hx >= N or hy < 0 or hy >= N or (hx, hy) in q:
        break
    q.append((hx, hy))
    if MAP[hx][hy] == 0:
        q.popleft()
    else:
        MAP[hx][hy] = 0

    if time == move[i][0]:
        if move[i][1] == "L":
            h = (h - 1) % 4
        else:
            h = (h + 1) % 4
        if i + 1 < len(move):
            i += 1

print(time)