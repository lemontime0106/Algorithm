def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    month_days = [31, 29, 31, 30, 31, 30, 
                  31, 31, 30, 31, 30, 31]
    
    total = 0
    
    for i in range(a - 1):
        total += month_days[i]
    
    total += b - 1
    
    return days[total % 7]