while True:
    N, M = map(int ,input().split())
    if N == 0 and M == 0:
        break
    else:
        edges = []

        for _ in range(M):
            a, b, c = map(int, input().split())
            edges.append((a, b, c))

        edges.sort(key=lambda x: x[2])

        parent = [i for i in range(N+1)]

        def find(x):
            if parent[x] != x:
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
            else:
                answer += c

        print(answer)
