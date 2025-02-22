import heapq

N = int(input())
q = []

for _ in range(N):
    a = list(map(int, input().split()))
    if not a[0]:
        if not len(q):
            print(-1)
        else:
            temp = -heapq.heappop(q)
            print(temp)
    else:
        for j in range(a[0]):
            heapq.heappush(q, -a[j+1])
