def find(parent, x):
    if parent[x] == x:
        return x

    return find(parent, parent[x])

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = []

    for _ in range(E):
        a, b, c = map(int, input().split())

        graph.append([c, a, b])

    graph.sort()
    parent = [i for i in range(V+1)]

    answer = 0

    for cost, a, b in graph:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost

    print(f"#{t} {answer}")