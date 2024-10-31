N, B = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

def mult(a, b):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += a[i][k] * b[k][j] % 1000
    return temp

def square(x, n):
    if n == 1:
        return x

    temp = square(x, n//2)
    if n % 2 == 0:
        return mult(temp, temp)
    else:
        return mult(mult(temp, temp), x)

answer = square(MAP, B)
for i in range(N):
    for j in range(N):
        answer[i][j] %= 1000

for a in answer:
    print(*a)