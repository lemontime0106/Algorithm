def fac(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

N = int(input())

for i in range(N):
    a, b = map(int, input().split())

    answer = fac(b) // (fac(a) * fac(b-a))
    print(answer)