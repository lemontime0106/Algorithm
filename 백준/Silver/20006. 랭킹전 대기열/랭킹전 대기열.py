P, M = map(int, input().split())

player = []
for _ in range(P):
    level, name = input().split()
    player.append([int(level), name])

rooms = []

for lv, n in player:
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == M:
            continue

        if rooms[i][0] - 10 <= lv <= rooms[i][0] + 10:
            flag = True
            rooms[i][1].append([lv, n])
            break
    if not flag:
        rooms.append([lv, [[lv, n]]])

for i in range(len(rooms)):
    if len(rooms[i][1]) == M:
        print('Started!')
        tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(M):
            print(*tmp_ids[j])
    else:
        print('Waiting!')
        tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(len(tmp_ids)):
            print(*tmp_ids[j])