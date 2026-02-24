import heapq

N = int(input())
lst = list(map(int, input().split()))

heapq.heapify(lst)

cost = 0

while len(lst) > 1:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)

    s = a + b
    cost += s

    heapq.heappush(lst, s)

print(cost)