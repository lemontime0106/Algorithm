import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        root[b] = a
        cnt[a] += cnt[b]
    print(cnt[a])

for _ in range(int(input())):
    N = int(input())
    root, cnt = {}, {}
    for i in range(N):
        a, b = input().split()
        if a not in root:
            root[a] = a
            cnt[a] = 1
        if b not in root:
            root[b] = b
            cnt[b] = 1
        union(a, b)
