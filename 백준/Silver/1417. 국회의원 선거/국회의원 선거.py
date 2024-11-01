import heapq

N = int(input())
D = int(input())
q = []

for _ in range(N-1):
    heapq.heappush(q, -int(input()))

answer = 0

while q:
    cnt = -heapq.heappop(q)
    if D > cnt:
        break

    D += 1
    answer += 1
    heapq.heappush(q, -(cnt-1))

print(answer)