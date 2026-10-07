def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        hour = schedules[i] // 100
        minute = schedules[i] % 100
        
        minute += 10
        
        if minute >= 60:
            hour += 1
            minute -= 60
            
        limit = hour * 100 + minute
        
        success = True
        
        for j in range(7):
            day = (startday - 1 + j) % 7 + 1
            
            if day >= 6:
                continue
                
            if timelogs[i][j] > limit:
                success = False
                break
        
        if success:
            answer += 1
    
    return answer