import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    n = int(input())
    if n == 0:
        if not heap:
            print(0)
        else:
            a, b = heapq.heappop(heap)
            print(-a)
    else:
        heapq.heappush(heap, (-n, i))
