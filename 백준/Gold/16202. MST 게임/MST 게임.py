def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    ra = find(parent, a)
    rb = find(parent, b)

    if ra == rb:
        return False

    if ra < rb:
        parent[rb] = ra
    else:
        parent[ra] = rb

    return True

N, M, K = map(int, input().split())
edges = []

for i in range(1, M+1):
    x, y = map(int, input().split())
    edges.append((i, x, y))

answer = []
start = 0

for _ in range(K):
    parent = list(range(N+1))
    mst_cost = 0
    cnt = 0
    first = -1

    for idx in range(start, M):
        cost, u, v = edges[idx]
        if union(parent, u, v):
            mst_cost += cost
            cnt += 1

            if first == -1:
                first = idx

            if cnt == N-1:
                break

    if cnt == N-1:
        answer.append(mst_cost)
        start = first + 1
    else:
        answer.extend([0] * (K - len(answer)))
        break

print(*answer)
