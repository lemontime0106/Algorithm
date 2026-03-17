N, M = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

g = gcd(N, M)
l = (N * M) // g

print(g)
print(l)