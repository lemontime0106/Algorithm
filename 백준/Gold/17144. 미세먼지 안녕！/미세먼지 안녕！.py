R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
cleaner = []

for i in range(R):
    if MAP[i][0] == -1:
        cleaner.append(i)

# 상하좌우 이동 방향
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread_dust():
    global MAP
    new_map = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if MAP[i][j] > 0:
                dust = MAP[i][j] // 5
                spread_count = 0
                for dx, dy in direct:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C and MAP[nx][ny] != -1:
                        new_map[nx][ny] += dust
                        spread_count += 1
                new_map[i][j] += MAP[i][j] - (dust * spread_count)
            elif MAP[i][j] == -1:
                new_map[i][j] = -1

    MAP = new_map

def clean_air():
    # 위쪽 공기청정기 (반시계 방향)
    top = cleaner[0]
    for i in range(top - 1, 0, -1):
        MAP[i][0] = MAP[i - 1][0]  # 위쪽 공기청정기: 왼쪽 열을 위로 이동
    for i in range(C - 1):
        MAP[0][i] = MAP[0][i + 1]  # 위쪽 공기청정기: 윗쪽 행을 왼쪽으로 이동
    for i in range(top):
        MAP[i][C - 1] = MAP[i + 1][C - 1]  # 위쪽 공기청정기: 오른쪽 열을 아래로 이동
    for i in range(C - 1, 1, -1):
        MAP[top][i] = MAP[top][i - 1]  # 위쪽 공기청정기: 아래쪽 행을 오른쪽으로 이동
    MAP[top][1] = 0  # 공기청정기에서 정화된 공기 배출

    # 아래쪽 공기청정기 (시계 방향)
    bottom = cleaner[1]
    for i in range(bottom + 1, R - 1):
        MAP[i][0] = MAP[i + 1][0]  # 아래쪽 공기청정기: 왼쪽 열을 아래로 이동
    for i in range(C - 1):
        MAP[R - 1][i] = MAP[R - 1][i + 1]  # 아래쪽 공기청정기: 아랫쪽 행을 왼쪽으로 이동
    for i in range(R - 1, bottom, -1):
        MAP[i][C - 1] = MAP[i - 1][C - 1]  # 아래쪽 공기청정기: 오른쪽 열을 위로 이동
    for i in range(C - 1, 1, -1):
        MAP[bottom][i] = MAP[bottom][i - 1]  # 아래쪽 공기청정기: 윗쪽 행을 오른쪽으로 이동
    MAP[bottom][1] = 0  # 공기청정기에서 정화된 공기 배출

for _ in range(T):
    spread_dust()
    clean_air()

# 남아있는 미세먼지의 양 계산
result = sum(sum(row) for row in MAP) + 2  # 공기청정기의 -1 값을 정확히 제외
print(result)
