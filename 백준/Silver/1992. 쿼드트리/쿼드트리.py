N = int(input())
MAP = [list(map(int, input())) for _ in range(N)]

answer = []

def solution(x, y, n):
    curr = MAP[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if MAP[i][j] != curr:
                answer.append("(")
                solution(x, y, n//2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                answer.append(")")
                return

    answer.append(str(curr))

solution(0, 0, N)
print("".join(answer))