def solution(stones, k):
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        skip = 0
        
        for stone in stones:
            if stone - mid <= 0:
                skip += 1
            else:
                skip = 0
                
            if skip >= k:
                break
        
        if skip >= k:
            right = mid - 1
        else:
            left = mid + 1
    
    return left
