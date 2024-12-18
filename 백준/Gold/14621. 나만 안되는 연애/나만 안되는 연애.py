def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
school = ["X"] + list(input().split())

parent = [i for i in range(N+1)]
edges = []

for _ in range(M):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()

answer = 0
cnt = 0

for d, u, v in edges:
    if school[u] != school[v] and find_parent(u) != find_parent(v):
        union(u, v)
        answer += d
        cnt += 1
    if cnt == N-1:
        break

print(answer) if cnt == N-1 else print(-1)

