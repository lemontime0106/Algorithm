import heapq

N = int(input())
lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort()

heap = []
for s, e in lst:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)

print(len(heap))