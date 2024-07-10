import heapq

N = int(input())

lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort(key=lambda x: (x[0], x[1]))
heap = [lst[0][1]]

for i in range(1, N):
    if heap[0] <= lst[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lst[i][1])

print(len(heap))