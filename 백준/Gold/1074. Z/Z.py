import sys
sys.setrecursionlimit(100000)


N, R, C = map(int, input().split())

N = 2 ** N


def solution(n, row, col):
    if n == 1:
        return 2 * row + col

    half = 2 ** (n - 1)

    if row < half and col < half:
        return solution(n-1, row, col)

    elif row < half <= col:
        return half * half + solution(n-1, row, col-half)

    elif row >= half > col:
        return 2 * half * half + solution(n-1, row-half, col)

    else:
        return 3 * half * half + solution(n-1, row - half, col - half)


print(solution(N, R, C))