import heapq

def solution(jobs):
    answer = 0
    now, i = 0, 0   # i => 처리한 일
    
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]]) # 짧은일 먼저 끝내기 (걸리는 시간, 시작 시간)
                
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
    
    return answer // len(jobs)