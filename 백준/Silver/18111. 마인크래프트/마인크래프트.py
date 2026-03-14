N, M, B = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

min_time = float("inf")
height = 0

for h in range(257):
    remove = 0
    add = 0

    for i in range(N):
        for j in range(M):
            if MAP[i][j] > h:
                remove += MAP[i][j] - h
            else:
                add += h - MAP[i][j]

    if B + remove >= add:
        time = remove * 2 + add

        if time < min_time or (time == min_time and h > height):
            min_time = time
            height = h

print(min_time, height)