N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
answer = 0

line_pairs = [
    [(-1,0), (1,0)],
    [(0,-1), (0,1)]
]

corner_pairs = [
    [(-1,0), (0,1)],
    [(-1,0), (0,-1)],
    [(1,0), (0,1)],
    [(1,0), (0,-1)]
]

for x in range(N):
    for y in range(M):
        for pair in line_pairs:
            total = grid[x][y]
            valid = True

            for dx, dy in pair:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    total += grid[nx][ny]
                else:
                    valid = False
                    break

            if valid:
                answer = max(answer, total) 

        for pair in corner_pairs:
            total = grid[x][y]
            valid = True

            for dx, dy in pair:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    total += grid[nx][ny]
                else:
                    valid = False
                    break

            if valid:
                answer = max(answer, total) 

print(answer)