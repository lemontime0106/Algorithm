from collections import deque

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, int(input()) + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    answer_room = 0
    answer_cnt = 0

    for x in range(N):
        for y in range(N):
            q = deque()
            q.append((x, y))

            cnt = 1

            while q:
                cx, cy = q.popleft()

                for dx, dy in direct:
                    nx = cx + dx
                    ny = cy + dy

                    if 0 <= nx < N and 0 <= ny < N:
                        if MAP[nx][ny] == MAP[cx][cy] + 1:
                            q.append((nx, ny))
                            cnt += 1

            if cnt > answer_cnt:
                answer_cnt = cnt
                answer_room = MAP[x][y]

            elif cnt == answer_cnt:
                answer_room = min(answer_room, MAP[x][y])

    print(f"#{t} {answer_room} {answer_cnt}")