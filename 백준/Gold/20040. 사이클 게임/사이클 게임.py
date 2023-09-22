import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra < rb:
        root[rb] = ra
    else:
        root[ra] = rb

N, M = map(int, input().split())
root = list(range(N))
flag = True
ans = 0

for i in range(1, M+1):
    x, y = map(int, input().split())

    if find(x) != find(y):
        union(x, y)
    else:
        flag = False
        ans = i
        break

if flag:
    print(0)
else:
    print(ans)