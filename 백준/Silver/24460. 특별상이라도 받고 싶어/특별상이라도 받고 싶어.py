N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

def solution(n, row, col):
    if n == 1:
        return MAP[row][col]
    else:
        temp = []

        temp.append(solution(n // 2, row, col))
        temp.append(solution(n // 2, row, col + n // 2))
        temp.append(solution(n // 2, row + n // 2, col))
        temp.append(solution(n // 2, row + n // 2, col + n // 2))
        return sorted(temp)[1]

print(solution(N, 0, 0))