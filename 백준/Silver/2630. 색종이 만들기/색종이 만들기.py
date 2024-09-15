N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

answer = []

def solution(x, y, N):
    color = MAP[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != MAP[i][j]:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        answer.append(0)
    else:
        answer.append(1)

solution(0, 0, N)
print(answer.count(0))
print(answer.count(1))
