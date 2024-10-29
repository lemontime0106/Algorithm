N = int(input())
M = int(input())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)