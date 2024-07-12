import heapq

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
heap = []
heapq.heapify(heap)

for i in lst:
    if len(heap) < M:
        heapq.heappush(heap, i)
    else:
        c = heapq.heappop(heap)
        heapq.heappush(heap, c + i)
print(max(heap))