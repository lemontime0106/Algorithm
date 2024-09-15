N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

answer = []

def solution(x, y, n):
    color = MAP[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if MAP[i][j] != color:
                temp = n // 3
                solution(x, y, temp)
                solution(x, y+temp, temp)
                solution(x, y+(2*temp), temp)
                solution(x+temp, y, temp)
                solution(x+temp, y+temp, temp)
                solution(x+temp, y+(temp*2), temp)
                solution(x+(2*temp), y, temp)
                solution(x+(2*temp), y+temp, temp)
                solution(x+(2*temp), y+(2*temp), temp)
                return

    answer.append(color)
    return

solution(0,0,N)

print(answer.count(-1))
print(answer.count(0))
print(answer.count(1))