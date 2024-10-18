def solution(diffs, times, limit):
    answer = float("inf")
    
    left, right = 1, 1000001 
    
    while left <= right:
        mid = (left + right) // 2  
        total_time = 0 
        flag = True 
        
        for i in range(len(diffs)):
            if diffs[i] > mid:
                mistakes = diffs[i] - mid
                if i == 0:
                    total_time += times[i] * (mistakes + 1)
                else:
                    total_time += (times[i] + times[i-1]) * mistakes + times[i]
            else:
                total_time += times[i]
                
            if total_time > limit:
                flag = False
                break
            
        if flag:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
