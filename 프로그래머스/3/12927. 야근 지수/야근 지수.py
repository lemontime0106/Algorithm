import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    
    answer = 0
    for i in works:
        answer += i ** 2
    
    return answer