def solution(priorities, location):
    answer = 0
    
    queue = [(v, i) for i, v in enumerate(priorities)]
    
    cnt = 0
    while True:
        a, idx = queue.pop(0)
        if any(a < q[0] for q in queue):
            queue.append((a, idx))
        else:
            cnt += 1
            if idx == location:
                answer = cnt
                break
    
    return answer