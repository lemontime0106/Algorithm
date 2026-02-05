import heapq

N, M = map(int, input().split())
MAP = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    MAP[a].append([b, c])

visited = [float("inf")] * (N+1)

heap = []
heapq.heappush(heap, (0, 1))

visited[1] = 0

while heap:
    cur_dist, cur = heapq.heappop(heap)

    if cur_dist > visited[cur]:
        continue

    for nxt, weight in MAP[cur]:
        nxt_dist = cur_dist + weight

        if nxt_dist < visited[nxt]:
            visited[nxt] = nxt_dist
            heapq.heappush(heap, (nxt_dist, nxt))

for i in range(2, N+1):
    if visited[i] == float("inf"):
        print(-1)
    else:
        print(visited[i])