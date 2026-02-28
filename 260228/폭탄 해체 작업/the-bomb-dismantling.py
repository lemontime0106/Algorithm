import heapq

N = int(input())

lst = [tuple(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: x[1])

heap = []

for score, deadline in lst:
    heapq.heappush(heap, score)

    if len(heap) > deadline:
        heapq.heappop(heap)

print(sum(heap))