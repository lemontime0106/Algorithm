N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

edges = []

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            edges.append((i+1, j+1, MAP[i][j]))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)