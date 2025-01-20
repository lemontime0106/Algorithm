N = int(input())
tree = []

for i in range(N):
    tree.append(int(input()))

answer = 0

gap = []

for i in range(N-1):
    gap.append(tree[i+1] - tree[i])

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

g = gap[0]

for i in range(1, len(gap)):
    g = gcd(g, gap[i])

for i in gap:
    answer += (i // g) - 1

print(answer)