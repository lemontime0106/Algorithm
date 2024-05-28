import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return cnt
        
        least = heapq.heappop(scoville)
        s_least = heapq.heappop(scoville)
        mix_state = least + (2 * s_least)
        heapq.heappush(scoville, mix_state)
        cnt += 1
    
    return cnt if scoville[0] >= K else -1
