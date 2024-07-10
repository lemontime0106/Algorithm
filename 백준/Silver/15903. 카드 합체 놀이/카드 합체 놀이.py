import heapq

N, M = map(int, input().split())
lst = list(map(int, input().split()))

heapq.heapify(lst)

for _ in range(M):
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    c = a + b
    for _ in range(2):
        heapq.heappush(lst, c)

print(sum(lst))
