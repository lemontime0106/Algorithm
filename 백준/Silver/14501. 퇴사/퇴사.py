N = int(input())

lst = [list(map(int ,input().split())) for _ in range(N)]

def solve(i):
    if i >= N:
        return 0
    ret = 0
    if i + lst[i][0] <= N:
        ret = solve(i + lst[i][0]) + lst[i][1]
    ret = max(ret, solve(i + 1))
    return ret

print(solve(0))