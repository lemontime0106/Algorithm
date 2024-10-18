def prim(start):
    global answer

    dist[0] = 0

    for _ in range(N):
        local_min = float("inf")
        for i in range(N):
            if not visited[i] and dist[i] < local_min:
                min_node = i
                local_min = dist[min_node]
        visited[min_node] = True
        answer += (E * local_min)

        for j in range(N):
            if not visited[j]:
                d = (X[min_node] - X[j]) ** 2 + (Y[min_node] - Y[j]) ** 2
                dist[j] = min(dist[j], d)


T = int(input())

for t in range(1, T+1):
    N = int(input())

    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    answer = 0
    visited = [False] * N
    dist = [float("inf")] * N
    prim(0)

    print(f"#{t} {round(answer)}")