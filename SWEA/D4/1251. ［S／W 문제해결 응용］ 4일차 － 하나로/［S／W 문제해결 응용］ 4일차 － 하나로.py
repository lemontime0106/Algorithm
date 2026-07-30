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

T = int(input())

for t in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    MAP = []

    for i in range(N):
        MAP.append([X[i], Y[i]])

    graph = []

    for i in range(N):
        for j in range(i+1, N):
            dx = MAP[i][0] - MAP[j][0]
            dy = MAP[i][1] - MAP[j][1]

            dist = dx ** 2 + dy ** 2

            graph.append((dist, i, j))

    graph.sort()

    parent = [i for i in range(N)]
    
    answer = 0

    for cost, a, b in graph:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)

            answer += cost

    answer = round(answer * E)

    print(f"#{t} {answer}")