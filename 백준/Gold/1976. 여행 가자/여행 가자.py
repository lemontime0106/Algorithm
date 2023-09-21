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

N = int(input())
M = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]
schedule = list(map(int, input().split()))
root = [0] + list(range(1, N+1))
lst = []
for i in range(1, M):
    lst.append((schedule[i-1], schedule[i]))

# 그래프 연결
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            union(i + 1, j + 1)

flag = True
for n1, n2 in lst:
    if find(n1) != find(n2):
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')