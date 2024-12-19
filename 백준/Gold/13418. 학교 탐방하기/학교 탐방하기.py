N, M = map(int, input().split())

edges = []

for _ in range(M+1):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# worst case
edges.sort(key=lambda x: x[0], reverse=True)
parent = [i for i in range(N+1)]
worst_cnt = 0
for c, a, b in edges:
    if find_parent(a) != find_parent(b):
        union(a, b)
        if c == 0:
            worst_cnt += 1
worst = worst_cnt ** 2

# best case
edges.sort(key=lambda x: x[0])
parent = [i for i in range(N+1)]
best_cnt = 0
for c, a, b in edges:
    if find_parent(a) != find_parent(b):
        union(a, b)
        if c == 0:
            best_cnt += 1
best = best_cnt ** 2

print(abs(worst - best))