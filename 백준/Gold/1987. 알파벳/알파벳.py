N, M = map(int, input().split())

MAP = [list(input()) for _ in range(N)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

root = set()
result = 0

def solution(x, y, cnt):
    global result
    if result < cnt:
        result = cnt
    if result == 26:
        print("26")
        exit(0)

    for d in direct:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] not in root:
            root.add(MAP[nx][ny])
            solution(nx, ny, cnt + 1)
            root.remove(MAP[nx][ny])

root.add(MAP[0][0])
solution(0, 0, 1)
print(result)
