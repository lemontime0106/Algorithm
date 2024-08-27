def solution(n, times):
    lst = []
    
    left, right = 1, max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        
        for time in times:
            cnt += mid // time
            
            if cnt == n:
                break
        
        if cnt >= n:
            lst.append(mid)
            right = mid - 1
        else:
            left = mid + 1
        
    return min(lst)