def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

N, M, K = map(int, input().split())
root = list(map(int, input().split()))

parent = [i for i in range(N+1)]

for r in root:
    union(parent, 0, r)

graph = []
for _ in range(M):
    s, e, d = map(int, input().split())
    graph.append((d, s, e))

answer = 0
graph.sort(key=lambda x: x[0])

for d, s, e in graph:
    if find_parent(parent, s) != find_parent(parent, e):
        union(parent, s, e)
        answer += d

print(answer)