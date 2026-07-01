import heapq

def to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(book_time):
    book_time.sort(key=lambda x: to_min(x[0]))
    
    heap = []
    
    for start, end in book_time:
        start = to_min(start)
        end = to_min(end) + 10
        
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        heapq.heappush(heap, end)
    
    return len(heap)