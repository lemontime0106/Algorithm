N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

def solution(x, y, n):
    if n == 2:
        answer = [MAP[x][y], MAP[x+1][y], MAP[x][y+1], MAP[x+1][y+1]]
        answer.sort()
        return answer[-2]
    temp = n // 2
    answer = [
        solution(x, y, temp),
        solution(x + temp, y, temp),
        solution(x, y + temp, temp),
        solution(x + temp, y + temp, temp)
    ]
    answer.sort()
    return answer[-2]

print(solution(0, 0, N))
