import heapq

N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))

heapq.heapify(lst)
answer = 0

while len(lst) > 1:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    c = a + b
    answer += c
    heapq.heappush(lst, c)

print(answer)