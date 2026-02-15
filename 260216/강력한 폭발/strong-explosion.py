N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

point = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            point.append((i, j))

bomb = [
    [(0,0), (-1,0), (1,0), (-2,0), (2,0)],  
    [(0,0), (0,-1), (0,1), (1,0), (-1,0)], 
    [(0,0), (-1,-1), (1,1), (1,-1), (-1,1)]   
]

max_area = 0
selected = []

def calculate():
    destroy = [[0] * N for _ in range(N)] 

    for idx in range(len(point)):
        x, y = point[idx]
        bomb_type = selected[idx]

        for dx, dy in bomb[bomb_type]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                destroy[nx][ny] = 1

    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += destroy[i][j]
    
    return cnt


def backtracking(idx):
    global max_area

    if idx == len(point):
        max_area = max(max_area, calculate())
        return

    for i in range(3):
        selected.append(i)
        backtracking(idx+1)
        selected.pop()

backtracking(0)
print(max_area)
