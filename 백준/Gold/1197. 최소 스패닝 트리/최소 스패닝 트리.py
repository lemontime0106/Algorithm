import sys
sys.setrecursionlimit(10 ** 5)

V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key = lambda x: x[2])

parent = [i for i in range(V+1)]

def find_parent(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return find_parent(a) == find_parent(b)

answer = 0

for a, b, cost in edges:
    if not same_parent(a, b):
        union(a, b)
        answer += cost

print(answer)