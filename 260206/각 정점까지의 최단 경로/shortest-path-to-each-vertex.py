import heapq

N, M = map(int, input().split())
K = int(input())

MAP = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    MAP[a].append([b, c])
    MAP[b].append([a, c])

visited = [float("inf")] * (N+1)
visited[K] = 0

heap = []
heapq.heappush(heap, (0, K))

while heap:
    cur_dist, cur = heapq.heappop(heap)

    if cur_dist > visited[cur]:
        continue
    
    for nxt, weight in MAP[cur]:
        new_dist = cur_dist + weight

        if new_dist < visited[nxt]:
            visited[nxt] = new_dist
            heapq.heappush(heap, (new_dist, nxt))

for i in visited[1:]:
    if i == float("inf"):
        print(-1)
    else:
        print(i)